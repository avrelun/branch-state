import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from provenance import MANIFEST, digest, inspect_provenance


class ProvenanceCheck(unittest.TestCase):
    def fixture(self):
        blobs = {'icon.svg': b'<svg/>', 'NOTICE.md': b'Palette source and MIT declaration'}
        entry = {
            'path': 'icon.svg', 'sha256': digest(blobs['icon.svg']),
            'evidence': 'Source and license inspected by test author',
            'sources': [{'kind': 'third-party', 'origin': 'https://example.invalid/palette/v1',
                         'author': 'Palette author', 'license': 'MIT', 'scope': 'Colors',
                         'notices': {'NOTICE.md': digest(blobs['NOTICE.md'])}}],
        }
        manifest = {'version': 1, 'assets': [entry]}
        blobs[MANIFEST] = json.dumps(manifest).encode()
        return blobs, manifest

    def test_recorded_asset_passes(self):
        self.assertEqual(inspect_provenance(self.fixture()[0]), [])

    def test_unrecorded_or_changed_assets_fail(self):
        for modification in ('missing_manifest', 'new_asset', 'changed_asset'):
            blobs, _ = self.fixture()
            if modification == 'missing_manifest':
                del blobs[MANIFEST]
            elif modification == 'new_asset':
                blobs['font.woff2'] = b'font fixture'
            else:
                blobs['icon.svg'] = b'<svg fill="red"/>'
            with self.subTest(modification=modification):
                self.assertTrue(inspect_provenance(blobs))

    def test_missing_or_changed_notice_fails(self):
        for notice in (None, b'', b'Different notice'):
            blobs, _ = self.fixture()
            if notice is None:
                del blobs['NOTICE.md']
            else:
                blobs['NOTICE.md'] = notice
            with self.subTest(notice=notice):
                self.assertTrue(inspect_provenance(blobs))

    def test_incomplete_claims_and_duplicate_entries_fail(self):
        for field in ('sources', 'evidence', 'author', 'license', 'origin', 'scope', 'notices', 'duplicate'):
            blobs, manifest = self.fixture()
            entry = manifest['assets'][0]
            if field == 'duplicate':
                manifest['assets'].append(entry.copy())
            elif field in ('sources', 'evidence'):
                del entry[field]
            else:
                del entry['sources'][0][field]
            blobs[MANIFEST] = json.dumps(manifest).encode()
            with self.subTest(field=field):
                self.assertTrue(inspect_provenance(blobs))

    def test_malformed_manifests_fail(self):
        for value in (b'{', b'[]', b'null', b'{"version": 1, "assets": null}'):
            with self.subTest(value=value):
                self.assertTrue(inspect_provenance({'icon.svg': b'<svg/>', MANIFEST: value}))

    def test_staged_and_committed_snapshots_not_working_tree(self):
        script = Path(__file__).with_name('check-publication.py').resolve()
        with tempfile.TemporaryDirectory() as directory:
            env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
            env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
            def git(*args):
                subprocess.run(['git', *args], cwd=directory, env=env,
                               check=True, capture_output=True)
            def check(*args):
                return subprocess.run(['python3', str(script), *args], cwd=directory,
                                      env=env, capture_output=True)
            git('init', '-q')
            blobs, _ = self.fixture()
            for name, content in blobs.items():
                path = Path(directory) / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            git('add', '.')
            (Path(directory) / 'NOTICE.md').unlink()
            self.assertEqual(check().returncode, 0)  # Indexed notice still exists.
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                'commit', '-qm', 'Asset fixture')
            (Path(directory) / 'icon.svg').write_bytes(b'<svg fill="red"/>')
            git('add', 'icon.svg')
            self.assertEqual(check().returncode, 1)  # Indexed asset no longer matches.
            result = check('--revision', 'HEAD')
            self.assertEqual(result.returncode, 0, result.stdout)
            # Exercise the real pre-push hook against good and bad committed tips.
            scripts = Path(directory) / 'scripts'
            scripts.mkdir()
            for filename in ('check-publication.py', 'provenance.py'):
                (scripts / filename).write_bytes((script.parent / filename).read_bytes())
            hook = script.parent.parent / '.githooks/pre-push'
            def push_check(oid):
                return subprocess.run(['sh', str(hook)], cwd=directory, env=env,
                                      input=f'refs/heads/topic {oid} refs/heads/topic {"0" * 40}\n',
                                      text=True, capture_output=True)
            good = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=directory, env=env, text=True).strip()
            self.assertEqual(push_check(good).returncode, 0)
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                'commit', '-qm', 'Changed asset without provenance update')
            bad = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=directory, env=env, text=True).strip()
            self.assertNotEqual(push_check(bad).returncode, 0)
            self.assertEqual(push_check('0' * 40).returncode, 0)  # Remote deletion.


if __name__ == '__main__':
    unittest.main()
