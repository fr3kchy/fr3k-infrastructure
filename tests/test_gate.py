import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from fr3k_control.gate import evaluate_gate, load_control


class GateTests(unittest.TestCase):
    def test_g0_blocks_unassigned_human_owners_and_open_p0_controls(self):
        control = {
            "gate": "G0",
            "controls": [
                {"id": "owner", "priority": "P0", "status": "BLOCKED", "owner": "Program Lead", "evidence": []},
                {"id": "rf", "priority": "P0", "status": "OPEN", "owner": "RF Lead", "evidence": []},
            ],
        }
        result = evaluate_gate(control)
        self.assertEqual("BLOCKED", result["verdict"])
        self.assertEqual(["owner", "rf"], result["blocking_controls"])

    def test_g0_passes_only_named_owners_closed_controls_and_existing_evidence(self):
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
                        "owner": "Michael Insch",
                        "evidence": [str(evidence)],
                    }
                ],
            }
            result = evaluate_gate(control)
            self.assertEqual("GO", result["verdict"])
            self.assertEqual([], result["blocking_controls"])

    def test_load_control_rejects_duplicate_control_ids(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "g0.json"
            path.write_text(json.dumps({"gate": "G0", "controls": [{"id": "x"}, {"id": "x"}]}))
            with self.assertRaisesRegex(ValueError, "duplicate control id"):
                load_control(path)


if __name__ == "__main__":
    unittest.main()
