# 🛠️ AI Log Analyzer (Kubernetes)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)
![Kubernetes](https://img.shields.io/badge/Domain-Kubernetes-326CE5)
![AIOps](https://img.shields.io/badge/Category-AIOps-purple)
![License](https://img.shields.io/badge/License-MIT-lightgray)

**Detects, explains and recommends fixes for Kubernetes failures automatically.**

A developer-friendly AIOps tool that reads Kubernetes/Ingress logs, flags known failure patterns (heuristics), and generates a concise **Root-Cause + Fix** report using an LLM. Built to demo your **AI + DevOps** skills in a real, impactful way.

---

## 🔥 Why this matters
Traditional log triage is slow and noisy. This tool turns raw logs into **actionable insights**:
- What happened (summary)
- Why it likely happened (probable root cause)
- **Exact kubectl/config fixes**
- Preventive next steps

Perfect for **portfolio**, **internal demos**, **interviews**, or as a stepping stone to **self-healing infra agents**.

---

## ✅ Features
- Detects **CrashLoopBackOff, OOMKilled, 5xx/502/504 errors, probe failures, failed mounts** and more
- Severity-aware **heuristic engine** with colored badges (Error/Warning/Info)
- **LLM-powered remediation steps** (gpt-4o-mini by default)
- Streamlit UI: **paste / upload / sample cards**
- One-click **Markdown RCA export**
- Kubernetes-focused design (SRE-grade)

---

## 🧠 Architecture
```mermaid
flowchart LR
    A[User Logs\n(Paste/Upload/Sample)] --> B[Parser]
    B --> C[Heuristics Engine\n(CrashLoopBackOff / OOM / 5xx / Mount / Probes)]
    B -->|raw text| D[LLM Prompt Builder]
    C -->|hints| D
    D --> E[OpenAI API\n(gpt-4o-mini)]
    E --> F[Markdown Report\nSummary • Root Cause • Fix • Next Steps]
    F --> G[Streamlit UI\nBadges + Download .md]
✨ Screenshots (Step-wise Showcase)
1️⃣ Logs Input (Sample Cards UI)
<p align="center"> <img src="docs/screenshots/1_input_cards.png" width="800"/> </p>
2️⃣ AI Analysis (Badges + RCA Summary)
<p align="center"> <img src="docs/screenshots/2_analysis_badges_rca.png" width="800"/> </p>
🚀 Quickstart
1️⃣ Clone & install
bash
Copy code
git clone https://github.com/komalrastogi/ai-log-analyzer.git
cd ai-log-analyzer
pip3 install -r requirements.txt
2️⃣ Set environment
bash
Copy code
echo "OPENAI_API_KEY=sk-xxxx" > .env
3️⃣ Run the UI
bash
Copy code
python3 -m streamlit run app/ui.py
🧪 Sample Logs Included
File	Scenario
k8s_sample.log	ImagePullBackOff + CrashLoopBackOff + OOM
k8s_probe_dns.log	Probe failures + DNSConfig issues + mount errors
nginx_5xx.log	Ingress 502/504 upstream failures

🧩 How it works
Component	Responsibility
parser.py	Converts raw logs → structured records
heuristics.py	Detects & classifies error patterns
ai_summary.py	Builds final LLM prompt using logs + hints
ui.py	Streamlit UI (cards, badges, export)

🧑‍💼 Resume-ready description
Developed an AI-based Kubernetes Log Analyzer using heuristic pattern detection (CrashLoopBackOff, OOMKilled, probe failures, ingress 5xx) and LLM reasoning to generate actionable root-cause and remediation guidance with a polished Streamlit UI.

🗺️ Roadmap
Phase	Feature
✅ Now	RCA + heuristics + UI export
Next	Self-healing (auto restart/scale/alerts)
Later	Multi-agent (Healer + Verifier)
Future	HuggingFace offline fallback

🙌 Acknowledgements
Inspired by real SRE/AIOps workflows:
logs → patterns → RCA → remediation → prevention

📜 License
MIT


