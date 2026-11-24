import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import LINE


class TestPatchNotes(unittest.TestCase):
    def test_line_within_gate(self):
        self.assertGreaterEqual(len(LINE), 1)
        self.assertLessEqual(len(LINE), 160)

    def test_line_is_one_line(self):
        self.assertNotIn("\n", LINE)
        self.assertTrue(LINE.strip())

    def test_line_is_patch_note_register(self):
        self.assertTrue(LINE.startswith("v"))
        self.assertIn("fixed a bug where", LINE)

    def test_main_rejects_out_of_gate_line(self):
        import main as main_mod

        original = main_mod.LINE
        try:
            main_mod.LINE = "x" * 161
            with self.assertRaises(SystemExit):
                main_mod.main()
        finally:
            main_mod.LINE = original

    def test_writes_exact_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            subprocess.run(
                [sys.executable, "main.py", out],
                check=True,
                cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            )
            with open(out, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), LINE)


if __name__ == "__main__":
    unittest.main()
