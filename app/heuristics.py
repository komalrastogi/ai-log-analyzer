# app/heuristics.py
import re
from typing import List, Dict

COMMON_PATTERNS = [
    (r"CrashLoopBackOff", "Pod is stuck in CrashLoopBackOff – container repeatedly failing to start."),
    (r"OOMKilled", "Container hit memory limit and was killed (OOMKilled)."),
    (r"ImagePullBackOff|Failed to pull image", "Image cannot be pulled – registry/auth or tag issue."),
    (r"Back[- ]off restarting", "Back-off restarting – repeated startup failures."),
    (r"502 Bad Gateway|5\d{2}", "5xx – upstream or backend service failing."),
    (r"FailedMount|MountVolume.SetUp failed", "Volume mount failure – PVC/hostPath/permissions."),
    (r"Liveness probe failed|Readiness probe failed", "Probe failure – application not responding."),
]

def run_heuristics(raw: str) -> List[Dict]:
    findings = []
    for pattern, hint in COMMON_PATTERNS:
        if re.search(pattern, raw, re.IGNORECASE):
            findings.append({"pattern": pattern, "hint": hint})
    return findings
