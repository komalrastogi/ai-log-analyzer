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
- **Exact commands** to fix (e.g., `kubectl`/config changes)
- Next steps to prevent recurrence

Perfect for: **portfolio, internal demos, interview stories, and AIOps POCs**.

---

## ✅ Features
- **K8s heuristics with severity** (badges): CrashLoopBackOff, OOMKilled, ImagePullBackOff, 5xx/502/504, FailedMount, Probe failures, etc.
- **LLM reasoning** (OpenAI `gpt-4o-mini` by default) to summarize and recommend fixes.
- **Streamlit UI**: paste logs / upload file / choose sample cards.
- **One-click report export** (`.md`) with timestamped filenames.
- **Stateless CLI ⇒ browser app**: no infra setup required.

---

## 🧠 Architecture

```mermaid
flowchart LR
    A[User Logs<br/>(Paste / Upload / Sample)] --> B[Parser]
    B --> C[Heuristics Engine<br/>(CrashLoopBackOff / OOM / 5xx / Mount / Probes)]
    B -->|raw log text| D[LLM Prompt Builder]
    C -->|hints| D
    D --> E[OpenAI API<br/>(gpt-4o-mini)]
    E --> F[Markdown RCA<br/>(Summary • Root Cause • Fix)]
    F --> G[Streamlit UI<br/>(Badges + Download)]
✨ Screenshots (Step-wise Showcase)
1️⃣ Logs Input (Sample Cards UI)
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; margin-bottom:20px;"> <p align="center"><strong>Logs Input (Sample Cards UI)</strong></p> <p align="center"><img src="docs/screenshots/1_input_cards.png" width="800"/></p> </div>
2️⃣ AI Analysis (Badges + RCA Summary)
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; margin-bottom:20px;"> <p align="center"><strong>AI Analysis (Badges + RCA Summary)</strong></p> <p align="center"><img src="docs/screenshots/2_analysis_badges_rca.png" width="800"/></p> </div>
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
🧪 Sample Logs
k8s_sample.log – mixed Kubernetes errors (ImagePullBackOff, CrashLoopBackOff, OOM)

k8s_probe_dns.log – probe failures + DNSConfig issues + mount errors

nginx_5xx.log – ingress 502/504 upstream failures + OOM

🧩 How it works
parser.py → Converts raw logs → structured records

heuristics.py → Detects & classifies error patterns with severity

ai_summary.py → Builds final LLM prompt using logs + hints

ui.py → Streamlit UI (cards, badges, markdown export)

🧑‍💼 Resume-ready description
Developed an AI-based Kubernetes Log Analyzer using heuristic pattern detection (CrashLoopBackOff, OOMKilled, probe failures, ingress 5xx) and LLM reasoning to generate actionable root-cause and remediation guidance via a polished UI.

🗺️ Roadmap
Self-healing actions (auto restart/scale/alerts)

Multi-agent (Healer + Validator)

HuggingFace offline fallback

🙌 Acknowledgements
Inspired by real SRE/AIOps workflows:
logs → patterns → RCA → remediation → prevention

📜 License
MIT
