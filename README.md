# 🛠️ AI Log Analyzer (Kubernetes)
**Detects, explains and recommends fixes for Kubernetes failures automatically.**

A developer-friendly AIOps tool that reads Kubernetes/Ingress logs, flags known failure patterns (heuristics), and generates a concise **Root-Cause + Fix** report using an LLM. Built to demo your **AI + DevOps** chops in minutes.

---

## 🔥 Why this matters
Traditional log triage is slow and noisy. This tool turns raw logs into **actionable steps**:
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
    A[User Logs\n(Paste/Upload/Sample)] --> B[Parser]
    B --> C[Heuristics Engine\n(CrashLoopBackOff / OOM / 5xx / Mount / Probes)]
    B -->|raw text| D[LLM Prompt Builder]
    C -->|hints| D
    D --> E[OpenAI API\n(gpt-4o-mini)]
    E --> F[Markdown Report\nSummary • Root Cause • Fix • Next Steps]
    F --> G[Streamlit UI\nBadges + Download .md]
```

---

## ✨ Screenshots (Step-wise Showcase)
> Put your real screenshots here after running the app.

1️⃣ **Logs Input (Cards)**
```
docs/screenshots/1_input_cards.png
```

2️⃣ **AI Analysis (Badges + RCA)**
```
docs/screenshots/2_analysis_badges_rca.png
```

> Tip (macOS): `⇧⌘4` to select an area. Save to `docs/screenshots/` and commit.

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

## 🧑‍💼 Resume-ready description
> **Developed an AI-based Kubernetes Log Analyzer** that uses pattern heuristics (CrashLoopBackOff, OOM, 5xx) and LLM reasoning to produce root-cause and step-by-step remediation.

---

## 🗺️ Roadmap
- Self-healing actions (restart/scale)
- Multi-agent (LangGraph/CrewAI)
- HuggingFace fallback

---

## 📜 License
MIT

