from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from render_views import rank_three_status_line  # noqa: E402


class RenderViewsTests(unittest.TestCase):
    def test_rank_three_status_before_terminal_sync(self) -> None:
        line = rank_three_status_line({"claims": [{"id": "CLM-073"}]})
        self.assertIn("`L14` remains open", line)
        self.assertNotIn("Orevkov", line)

    def test_rank_three_status_after_terminal_sync(self) -> None:
        line = rank_three_status_line(
            {"claims": [{"id": "CLM-073"}, {"id": "CLM-074"}, {"id": "CLM-078"}]}
        )
        self.assertIn("Orevkov", line)
        self.assertIn("`CLM-078` is a `literature_bound` application", line)
        self.assertIn("No degree-four-or-higher or `JC_2` result follows", line)


if __name__ == "__main__":
    unittest.main()
