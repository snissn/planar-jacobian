from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from render_views import rank_three_status_line, rank_three_terminal_claims  # noqa: E402


class RenderViewsTests(unittest.TestCase):
    def test_rank_three_status_before_terminal_sync(self) -> None:
        line = rank_three_status_line(
            {
                "claims": [
                    {"id": "CLM-073"},
                    {
                        "id": "CLM-074",
                        "track": "another-track",
                        "statement": "An unrelated packet allocated this ID.",
                    },
                ]
            }
        )
        self.assertIn("`L14` remains open", line)
        self.assertNotIn("Orevkov", line)

    def test_rank_three_status_after_terminal_sync(self) -> None:
        claims = [
            {
                "id": "CLM-080",
                "track": "low-degree-literature",
                "statement": "Orevkov excludes planar Keller function-field degree three.",
                "note": "R3BC-01",
            },
            {"id": "CLM-081", "note": "R3BC-02"},
            {"id": "CLM-082", "note": "R3BC-03"},
            {"id": "CLM-083", "note": "R3BC-04"},
            {"id": "CLM-084", "note": "R3BC-05"},
        ]
        line = rank_three_status_line({"claims": claims})
        self.assertIn("Orevkov", line)
        self.assertIn("`CLM-080` excludes", line)
        self.assertIn("`CLM-081`, `CLM-082`, `CLM-083`", line)
        self.assertIn("`CLM-084` is a `literature_bound` application", line)
        self.assertIn("No degree-four-or-higher or `JC_2` result follows", line)

    def test_rank_three_terminal_semantics_do_not_reserve_an_id(self) -> None:
        claims = [
            {
                "id": "CLM-074",
                "track": "another-track",
                "statement": "Unrelated claim.",
            },
            {
                "id": "CLM-091",
                "track": "low-degree-literature",
                "statement": "Orevkov excludes function-field degree three.",
            },
        ]
        self.assertEqual(["CLM-091"], [item["id"] for item in rank_three_terminal_claims(claims)])


if __name__ == "__main__":
    unittest.main()
