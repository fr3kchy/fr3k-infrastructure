from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PASS_STATUS = "CLOSED"
ROLE_MARKERS = (" lead", " team", " board", " group", " owner", " maintainer", " controller")
PLACEHOLDER_OWNERS = {
    "unassigned",
    "tbd",
    "tba",
    "unknown",
    "none",
    "n/a",
    "na",
    "placeholder",
    "human",
    "operator",
    "core team",
    "program lead",
    "rf lead",
}


def load_control(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    controls = data.get("controls")
    if not isinstance(controls, list):
        raise ValueError("controls must be a list")
    ids = [item.get("id") for item in controls]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate control id")
    data["_base_dir"] = str(path.parent)
    return data


def _named_human(control: dict[str, Any]) -> bool:
    # owner_type is a claim about the owner, not evidence that a concrete owner
    # has actually been named. Validate the value first, regardless of type.
    owner = " ".join(str(control.get("owner", "")).strip().split()).lower()
    if not owner or owner in PLACEHOLDER_OWNERS:
        return False
    if owner.startswith(("tbd ", "tba ", "unassigned ", "placeholder ", "example ", "test ")):
        return False
    if any(owner.endswith(marker) for marker in ROLE_MARKERS):
        return False
    return True


def _evidence_exists(control: dict[str, Any], base_dir: Path) -> bool:
    evidence = control.get("evidence", [])
    if not evidence:
        return False
    return all((Path(item) if Path(item).is_absolute() else base_dir / item).exists() for item in evidence)


def evaluate_gate(control: dict[str, Any]) -> dict[str, Any]:
    base_dir = Path(control.get("_base_dir", "."))
    evaluated = []
    blockers = []
    for item in control["controls"]:
        status_ok = item.get("status") == PASS_STATUS
        owner_ok = _named_human(item)
        evidence_ok = _evidence_exists(item, base_dir)
        passed = status_ok and owner_ok and evidence_ok
        evaluated.append({
            "id": item["id"],
            "passed": passed,
            "status_ok": status_ok,
            "owner_ok": owner_ok,
            "evidence_ok": evidence_ok,
        })
        if item.get("priority") == "P0" and not passed:
            blockers.append(item["id"])
    return {
        "gate": control.get("gate", "UNKNOWN"),
        "verdict": "GO" if not blockers else "BLOCKED",
        "blocking_controls": blockers,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "controls": evaluated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate an FR3K decision gate")
    parser.add_argument("control", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate_gate(load_control(args.control))
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["verdict"] == "GO" else 2


if __name__ == "__main__":
    raise SystemExit(main())
