import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from fr3k_control.gate import evaluate_gate


class PlaceholderOwnerTests(unittest.TestCase):
    def test_owner_type_human_does_not_bypass_placeholder_rejection(self):
        with TemporaryDirectory() as tmp:
            evidence = Path(tmp) / "signoff.md"
            evidence.write_text("approved\n")
            control = {
                "gate": "G0",
                "controls": [
                    {
                        "id": "owner",
                        "priority": "P0",
                        "status": "CLOSED",
                        "owner_type": "human",
                        "owner": "TBD",
                        "evidence": [str(evidence)],
                    }
                ],
            }
            result = evaluate_gate(control)
            self.assertEqual("BLOCKED", result["verdict"])
            self.assertFalse(result["controls"][0]["owner_ok"])


if __name__ == "__main__":
    unittest.main()
