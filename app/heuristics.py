# app/heuristics.py
import re
from typing import List, Dict

# pattern, hint, severity
RULES = [
    (r"OOMKilled", "Container exceeded memory limit (OOMKilled).", "error"),
    (r"502 Bad Gateway|5\d{2}\b", "Upstream/service returning 5xx.", "error"),
    (r"CrashLoopBackOff", "Pod stuck in CrashLoopBackOff.", "warning"),
    (r"ImagePullBackOff|Failed to pull image", "Image pull/registry or tag issue.", "warning"),
    (r"Back[- ]off restarting", "Back-off: container repeatedly failing to start.", "warning"),
    (r"FailedMount|MountVolume.SetUp failed", "Volume mount failure (PVC/hostPath/permissions).", "warning"),
    (r"Liveness probe failed|Readiness probe failed", "Probe failure – app not responding / probe misconfig.", "warning"),
    (r"\bStarted\b|\bPulling\b|\bCreated\b", "Informational event.", "info"),
]

def run_heuristics(raw: str) -> List[Dict]:
    findings: List[Dict] = []
    for pattern, hint, sev in RULES:
        if re.search(pattern, raw, re.IGNORECASE):
            findings.append({"pattern": pattern, "hint": hint, "severity": sev})
    return findings

