#!/usr/bin/env python3
"""Verify g0-result.json is fresh, excluding volatile evaluated_at field."""
import json
import subprocess
import sys

committed = subprocess.run(
    ['git', 'show', 'HEAD:evidence/g0-result.json'],
    capture_output=True, text=True, check=True,
)
regenerated = open('evidence/g0-result.json').read()

c = json.loads(committed.stdout)
r = json.loads(regenerated)

c.pop('evaluated_at', None)
r.pop('evaluated_at', None)

if c != r:
    print('FAIL: evidence/g0-result.json differs (excluding timestamps)')
    sys.exit(1)
print('OK: evidence/g0-result.json is fresh (excluding volatile evaluated_at)')