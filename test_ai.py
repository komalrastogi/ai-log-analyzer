from app.parser import load_logs
from app.heuristics import run_heuristics
from app.ai_summary import summarize_logs

path = "data/sample_logs/k8s_sample.log"
raw = open(path).read()
heur = run_heuristics(raw)

print("HEURISTICS DETECTED:", heur, "\n")
print("=== AI SUMMARY REPORT ===\n")
print(summarize_logs(raw, heur))

