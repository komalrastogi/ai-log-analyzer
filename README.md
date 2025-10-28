# 🛠️ AI Log Analyzer (Kubernetes)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)
![Kubernetes](https://img.shields.io/badge/Domain-Kubernetes-326CE5)
![AIOps](https://img.shields.io/badge/Category-AIOps-purple)
![License](https://img.shields.io/badge/License-MIT-lightgray)

**Detects, explains and recommends fixes for Kubernetes failures automatically.**

A developer-friendly AIOps tool that reads Kubernetes/Ingress logs, flags known failure patterns, and produces a concise **Root-Cause + Fix** report using LLM reasoning.

---

## 🔥 Why this matters

Traditional log triage is slow and noisy. This tool turns logs into **actionable insights**:
- What happened (summary)
- Why it happened (probable root cause)
- Exact kubectl/config fix steps
- How to prevent recurrence

Perfect for **portfolio**, **interviews**, and **AIOps proof-of-concepts**.

---

## ✅ Features

- Detects CrashLoopBackOff / OOMKilled / 5xx / Mount / Probe failures
- LLM-powered remediation guidance (OpenAI `gpt-4o-mini`)
- Paste logs / upload / sample cards
- One-click Markdown export
- No infra setup — runs locally via Streamlit

---

## 🧠 Architecture

```mermaid

graph LR
    A[User Logs (Paste / Upload / Sample)] --> B[Parser]
    B --> C[Heuristics Engine (CrashLoopBackOff / OOM / 5xx / Probes)]
    B -->|raw text| D[LLM Prompt Builder]
    C -->|hints| D
    D --> E[OpenAI API (gpt-4o-mini)]
    E --> F[Markdown RCA (Root Cause + Fix)]
    F --> G[Streamlit UI (Badges + Download)]
```

✨ Screenshots
1️⃣ Logs Input (Sample Cards UI)
<table width="100%"> <tr><td align="center" style="border:1px solid #e5e7eb; border-radius:10px; padding:14px;"> <b>Logs Input (Sample Cards UI)</b><br/><br/> <img src="docs/screenshots/1_input_cards.png" width="820"/> </td></tr> </table>
2️⃣ AI Analysis (Badges + RCA Summary)
<table width="100%"> <tr><td align="center" style="border:1px solid #e5e7eb; border-radius:10px; padding:14px;"> <b>AI Analysis (Badges + RCA Summary)</b><br/><br/> <img src="docs/screenshots/2_analysis_badges_rca.png" width="820"/> </td></tr> </table>
🚀 Quickstart
<details> <summary><b>Click to expand installation steps</b></summary>
✅ 1) Clone & install
bash
Copy code
git clone https://github.com/komalrastogi/ai-log-analyzer.git
cd ai-log-analyzer
pip3 install -r requirements.txt
🔐 2) Set OpenAI key
bash
Copy code
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxx" > .env
▶️ 3) Run
bash
Copy code
python3 -m streamlit run app/ui.py
</details>
🧪 Sample Logs
📄 File	⚙️ Scenario
k8s_sample.log	Mixed K8s errors (ImagePullBackOff, CrashLoopBackOff, OOM)
k8s_probe_dns.log	Probe + DNSConfig + Mount failures
nginx_5xx.log	Ingress upstream 502/504

🧩 How it works
parser.py → parses raw logs

heuristics.py → detects known failure patterns

ai_summary.py → builds RCA prompt for LLM

ui.py → Streamlit frontend + export

🧑‍💼 Resume-ready summary
Built an AI-based Kubernetes Log Analyzer using heuristic detection + LLM reasoning to generate actionable RCA with fix steps via a polished Streamlit UI.

🗺️ Roadmap
Auto-healing (restart / scale)

Agent-based workflows (LangGraph/CrewAI)

HuggingFace offline models

📜 License
MIT

