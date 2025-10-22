# app/parser.py
"""
Log parser for AI Log Analyzer.

Reads a log file (k8s_sample.log) and returns structured records in memory
(as a list of dicts). Robust to noisy lines and long messages.
"""

import re
from typing import List, Dict, Optional
from datetime import datetime

# Regex to capture: timestamp, source (name), pid, level, message
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+'
    r'(?P<source>[^\[]+)\[(?P<pid>\d+)\]:\s+'
    r'(?P<level>\w+)\s+(?P<message>.+)'
)

def parse_log_line(line: str) -> Optional[Dict]:
    """Parse one line. Returns dict or None if no match."""
    line = line.strip()
    if not line:
        return None
    m = LOG_PATTERN.search(line)
    if not m:
        # fallback: try to capture timestamp + rest
        parts = line.split(' ', 1)
        if len(parts) == 2 and parts[0].endswith('Z'):
            return {"timestamp": parts[0], "source": None, "pid": None, "level": None, "message": parts[1]}
        return None
    d = m.groupdict()
    return {
        "timestamp": d.get("timestamp"),
        "source": d.get("source").strip(),
        "pid": d.get("pid"),
        "level": d.get("level"),
        "message": d.get("message").strip(),
    }

def load_logs(path: str) -> List[Dict]:
    """
    Load and parse a log file into a list of records.
    Each record: {timestamp, source, pid, level, message}
    """
    records: List[Dict] = []
    with open(path, "r", errors="ignore") as fh:
        for line in fh:
            parsed = parse_log_line(line)
            if parsed:
                records.append(parsed)
    return records

def summarize_counts(records: List[Dict]) -> Dict[str,int]:
    """Return simple counts (by level) for quick overview."""
    counts = {}
    for r in records:
        lvl = r.get("level") or "UNKNOWN"
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

if __name__ == "__main__":
    path = "data/sample_logs/k8s_sample.log"
    print(f"Loading logs from: {path}")
    recs = load_logs(path)
    print(f"Total parsed records: {len(recs)}\n")
    # show first 5 records
    for i, r in enumerate(recs[:5], start=1):
        print(f"[{i}] {r['timestamp']} {r['source']} {r['level']} {r['message'][:120]}")
    print("\nCounts by level:")
    print(summarize_counts(recs))
