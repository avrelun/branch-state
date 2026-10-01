# SPDX-License-Identifier: MIT
"""Protect local credentials from overwrite and accidental broad file access."""

from pathlib import Path
import stat
import tempfile
import unittest

from init_local_env import create_env


class LocalEnvTests(unittest.TestCase):
    def test_credentials_are_private_and_existing_file_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = root / ".env.example"
            template.write_text("POSTGRES_USER=branchstate\nPOSTGRES_PASSWORD=\n")
            destination = root / ".env"
            create_env(destination, template)
            original = destination.read_bytes()
            self.assertNotIn(b"POSTGRES_PASSWORD=\n", original)
            self.assertEqual(stat.S_IMODE(destination.stat().st_mode), 0o600)
            with self.assertRaises(FileExistsError):
                create_env(destination, template)
            self.assertEqual(destination.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
