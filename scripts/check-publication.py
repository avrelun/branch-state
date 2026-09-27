#!/usr/bin/env python3
"""Check indexed or committed blobs without printing possible secret contents."""
import argparse
import pathlib
import re
import subprocess
import sys

from provenance import inspect_provenance

LOCAL_PREFIXES = ('docs/operations/', 'docs/research/', 'docs/work/', 'assets/', '.wrangler/')
LOCAL_FILES = {'ROADMAP.md', 'docs/NEXT_SESSION.md', 'branchstate-starter.zip'}
PATTERNS = [
    re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
    re.compile(rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b'),
    re.compile(rb'\bgithub_pat_[A-Za-z0-9_]{40,}\b'),
    re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    re.compile(rb'\bglpat-[A-Za-z0-9_-]{20,}\b'),
]


def git(*args):
    return subprocess.check_output(['git', *args])


def inspect(path, mode, data):
    p = pathlib.PurePosixPath(path)
    reasons = []
    if path.startswith(LOCAL_PREFIXES) or path in LOCAL_FILES:
        reasons.append('local-only material')
    if (p.name == '.env' or p.name.startswith('.env.')) and p.name != '.env.example':
        reasons.append('environment file')
    if p.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.eml', '.pdf', '.zip'}:
        reasons.append('credential, evidence, or archive needs explicit review')
    if mode in {'120000', '160000'}:
        reasons.append('symlink or submodule needs explicit review')
    if len(data) > 2 * 1024 * 1024:
        reasons.append('blob exceeds 2 MiB review limit')
    if any(pattern.search(data) for pattern in PATTERNS):
        reasons.append('possible credential')
    if b'\x00' not in data:
        for line in data.splitlines():
            if line.rstrip(b' \t') != line:
                reasons.append('trailing whitespace')
                break
    return reasons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', help='Check a committed tree instead of the index')
    args = parser.parse_args()
    if args.revision:
        revision = git('rev-parse', '--verify', '--end-of-options', args.revision + '^{commit}').decode().strip()
        records = git('ls-tree', '-rz', revision).split(b'\0')
    else:
        records = git('ls-files', '--stage', '-z').split(b'\0')
    failed = False
    count = 0
    blobs = {}
    for record in filter(None, records):
        metadata, raw_path = record.split(b'\t', 1)
        fields = metadata.decode().split()
        if args.revision:
            mode, kind, oid = fields
        else:
            mode, oid, stage = fields
            kind = 'commit' if mode == '160000' else 'blob'
            if stage != '0':
                print('FAIL: unresolved index entries')
                return 1
        path = raw_path.decode('utf-8', errors='surrogateescape')
        data = git('cat-file', 'blob', oid) if kind == 'blob' else b''
        if kind == 'blob':
            blobs[path] = data
        reasons = inspect(path, mode, data)
        count += 1
        if reasons:
            print(f'FAIL {path!r}: {", ".join(reasons)}')
            failed = True
    if not count:
        print('FAIL: no files to inspect')
        return 1
    for reason in inspect_provenance(blobs):
        print(f'FAIL: {reason}')
        failed = True
    print(f'Inspected {count} blobs; {"FAIL" if failed else "PASS"}. Heuristic checks do not establish licensing or absence of secrets.')
    return int(failed)


if __name__ == '__main__':
    sys.exit(main())
