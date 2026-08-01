from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

REQUIRED = {
    "README.md",
    "FR3K_SOP_and_Template_Manual_v1.1.md",
    "FR3K_Master_Strategic_Report_v1.1.md",
    "FR3K_SeaArt_Prompt_Library_v1.1.json",
    "FR3K_Execution_Workbook_v1.1.xlsx",
    "FR3K_Source_Register_v1.1.csv",
    "SHA256SUMS.txt",
}


def audit(pack: Path) -> dict:
    missing = sorted(name for name in REQUIRED if not (pack / name).is_file())
    checksum_failures = []
    manifest = pack / "SHA256SUMS.txt"
    if manifest.is_file():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            expected, name = line.split(maxsplit=1)
            target = pack / name.strip().lstrip("*")
            if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
                checksum_failures.append(name.strip())

    readme = (pack / "README.md").read_text(encoding="utf-8") if not missing else ""
    prompt_match = re.search(r"SeaArt prompt records\s*\|\s*(\d+)", readme)
    declared_prompts = int(prompt_match.group(1)) if prompt_match else None
    library_path = pack / "FR3K_SeaArt_Prompt_Library_v1.1.json"
    library = json.loads(library_path.read_text(encoding="utf-8")) if library_path.is_file() else {}
    actual_prompts = len(library.get("prompts", []))
    sop_path = pack / "FR3K_SOP_and_Template_Manual_v1.1.md"
    sop_text = sop_path.read_text(encoding="utf-8") if sop_path.is_file() else ""
    findings = []
    if declared_prompts != actual_prompts:
        findings.append(f"prompt count mismatch: README={declared_prompts}, JSON={actual_prompts}")
    if "[... SOP Content Retained ...]" in sop_text:
        findings.append("SOP manual contains a placeholder instead of SOP-01 through SOP-25 procedures")
    return {
        "integrity": "PASS" if not missing and not checksum_failures else "FAIL",
        "missing": missing,
        "checksum_failures": checksum_failures,
        "declared_prompt_count": declared_prompts,
        "actual_prompt_count": actual_prompts,
        "findings": findings,
        "operational_acceptance": "BLOCKED" if findings or missing or checksum_failures else "READY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit FR3K implementation-pack integrity and consistency")
    parser.add_argument("pack", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.pack)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["operational_acceptance"] == "READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
