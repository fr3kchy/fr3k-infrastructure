# FR3K Infrastructure

Operational control plane for **Free Communications. Open Infrastructure. AI Driven. Community Built.**

This repository converts Implementation Pack v1.1 into executable gates and evidence. It does **not** authorise RF transmission, procurement, or field deployment.

## Current status

- Pack checksum integrity: PASS
- Pack operational consistency: BLOCKED
- G0 decision gate: BLOCKED
- Existing Reticulum/LXMF virtual/LAN baseline: ACCEPTED
- Physical RF/RNode: NOT TESTED

## Run

```bash
python3 -m unittest discover -s tests -v
python3 -m fr3k_control.pack_audit docs/source-pack/v1.1 --output evidence/pack-audit.json
python3 -m fr3k_control.gate control/gates/g0.json --output evidence/g0-result.json
```

A non-zero exit from either operational check is intentional while blockers exist.

## Hard boundaries

1. Reticulum/LXMF transport remains independent of Hermes and optional services.
2. No transmission or deployment without an exact RF configuration and current ACMA review.
3. No public/third-party installation without written authority and maintenance/removal ownership.
4. No AI-generated artefact is deployment evidence.
5. No P0 control closes without a named human and retained evidence.

## Related technical baseline

[`fr3kchy/hermes-reticulum-platform`](https://github.com/fr3kchy/hermes-reticulum-platform) is the accepted virtual/LAN gateway baseline. FR3K governance and field acceptance live here; transport implementation remains separate.
