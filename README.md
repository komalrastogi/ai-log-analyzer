# 🛠️ AI Log Analyzer (Kubernetes)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)
![Kubernetes](https://img.shields.io/badge/Domain-Kubernetes-326CE5)
![AIOps](https://img.shields.io/badge/Category-AIOps-purple)
![License](https://img.shields.io/badge/License-MIT-lightgray)

**Detects, explains and recommends fixes for Kubernetes failures automatically.**  
An AIOps tool that parses Kubernetes/Ingress logs, detects known failure signals, and generates a concise **Root-Cause + Remediation** report using LLM reasoning.

---

## 🔥 Why this matters

Traditional log triage is slow, repetitive, and noisy.  
This tool converts raw logs into **actionable RCA**:

| Insight | Delivered |
|--------|-----------|
| What broke? | Summary |
| Why? | Probable Root Cause |
| How to fix? | kubectl/config steps |
| Prevention? | Next steps |

---

## ✅ Features

- Detects **CrashLoopBackOff / OOMKilled / 5xx / Probe / Mount failures**
- Heuristic-based **severity badging** (🔴 error / 🟠 warning / 🟢 info)
- LLM-powered RCA via `gpt-4o-mini`
- Paste logs / Upload / Built-in **sample cards**
- One-click **Markdown export**
- Runs locally — no infra required

---

## 🧠 Architecture

```mermaid
flowchart LR
A[Logs Input (Paste / Upload / Sample)] --> B[Parser]
B --> C[Heuristics Engine]
B -->|raw logs| D[Prompt Builder]
C -->|hints| D
D --> E[OpenAI LLM]
E --> F[RCA Markdown Report]
F --> G[Streamlit UI (Badges + Export)]
```

---

## ✨ Screenshots (Step-wise Showcase) 


1️⃣ Logs Input (Sample Cards UI)
<table width="100%"> <tr><td align="center" style="border:1px solid #e5e7eb; border-radius:10px; padding:14px;"> <img src="docs/screenshots/1_input_cards.png" width="820"/> </td></tr> </table>
2️⃣ AI Analysis (Badges + RCA Summary)
<table width="100%"> <tr><td align="center" style="border:1px solid #e5e7eb; border-radius:10px; padding:14px;"> <img src="docs/screenshots/2_analysis_badges_rca.png" width="820"/> </td></tr> </table>

---

## 🚀 Quickstart

### 1) Clone & install
```bash
git clone https://github.com/komalrastogi/ai-log-analyzer.git
cd ai-log-analyzer
pip3 install -r requirements.txt
```

### 2) Set your OpenAI key
```bash
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxx" > .env
```

### 3) Run
```bash
python3 -m streamlit run app/ui.py
```

---

## 🧪 Sample Logs
- `k8s_sample.log` – mixed issues
- `k8s_probe_dns.log` – probe + DNS + mount
- `nginx_5xx.log` – ingress + latency + restart

---
##  🧩 How it works
Component
Role
parser.py
Parses raw logs
heuristics.py
Detects known failure signals
ai_summary.py
Builds RCA prompt for LLM
ui.py
Streamlit frontend

---

## 🧑‍💼 Resume-ready description
> **Developed an AI-based Kubernetes Log Analyzer using heuristic detection + LLM reasoning to generate root-cause explanations and step-by-step remediation guidance with a Streamlit UI front-end.

---

## 🗺️ Roadmap
- Self-healing actions (restart/scale)
- Multi-agent (LangGraph/CrewAI)
- HuggingFace fallback

---

## 🙌 Acknowledgements
This project is a stepping stone toward self-healing Kubernetes — evolving from observability to autonomous remediation.

---

## 📜 License
MIT

