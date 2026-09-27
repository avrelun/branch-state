import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('check-publication.py').resolve()
SPEC = importlib.util.spec_from_file_location('guard', SCRIPT)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class PublicationCheck(unittest.TestCase):
    def test_allowed_example(self):
        self.assertEqual(guard.inspect('.env.example', '100644', b'PORT=8000\n'), [])

    def test_private_paths(self):
        for path in ['docs/operations/bill.md', '.env.local', 'backup.zip', 'assets/avatar.png']:
            with self.subTest(path=path):
                self.assertTrue(guard.inspect(path, '100644', b''))

    def test_credential_detection_without_echo(self):
        secret = b'gh' + b'p_' + b'A' * 36
        self.assertIn('possible credential', guard.inspect('config.txt', '100644', secret))

    def test_symlink_rejected(self):
        self.assertTrue(guard.inspect('external', '120000', b'/tmp/external'))

    def test_index_is_checked_instead_of_working_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
            env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
            def git(*args):
                return subprocess.run(['git', *args], cwd=directory, env=env, check=True, capture_output=True)
            git('init', '-q')
            path = Path(directory) / 'config.txt'
            secret = b'gh' + b'p_' + b'A' * 36
            path.write_bytes(secret)
            git('add', 'config.txt')
            path.write_text('clean working copy\n')
            result = subprocess.run(['python3', str(SCRIPT)], cwd=directory, env=env, capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn(secret, result.stdout)
            path.write_text('safe\n')
            git('add', 'config.txt')
            result = subprocess.run(['python3', str(SCRIPT)], cwd=directory, env=env, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout)
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'Fixture')
            path.write_bytes(secret)
            git('add', 'config.txt')
            result = subprocess.run(['python3', str(SCRIPT), '--revision', 'HEAD'], cwd=directory, env=env, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout)


if __name__ == '__main__':
    unittest.main()
