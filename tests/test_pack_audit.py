import unittest
from pathlib import Path

from fr3k_control.pack_audit import audit


class PackAuditTests(unittest.TestCase):
    def test_imported_v11_pack_is_intact_but_not_operationally_accepted(self):
        pack = Path(__file__).parents[1] / "docs" / "source-pack" / "v1.1"
        result = audit(pack)
        self.assertEqual("PASS", result["integrity"])
        self.assertEqual("BLOCKED", result["operational_acceptance"])
        self.assertEqual(240, result["declared_prompt_count"])
        self.assertEqual(236, result["actual_prompt_count"])
        self.assertEqual([], result["checksum_failures"])


if __name__ == "__main__":
    unittest.main()
