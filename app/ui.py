# app/ui.py
import streamlit as st
from pathlib import Path
from datetime import datetime
from app.heuristics import run_heuristics
from app.ai_summary import summarize_logs

st.set_page_config(page_title="AI Log Analyzer", layout="wide")
st.title("🛠️ AI Log Analyzer (Kubernetes)")
st.caption("Paste logs • Upload file • Use sample • Export AI RCA report (.md)")

ss = st.session_state
ss.setdefault("last_report", "")
ss.setdefault("last_filename", "log")
ss.setdefault("last_heuristics", [])
ss.setdefault("active_tab", "logs")   # 'logs' or 'analysis'

# --- helper: colored badge HTML ---
def badge(text: str, sev: str) -> str:
    colors = {
        "error":   "#B91C1C",  # red-700
        "warning": "#D97706",  # amber-600
        "info":    "#15803D",  # green-700
    }
    bg = colors.get(sev, "#334155")
    return (
        f'<span style="display:inline-block;padding:4px 10px;'
        f'border-radius:999px;background:{bg};color:#fff;'
        f'font-size:12px;margin:0 6px 6px 0;">{text}</span>'
    )

# ---- view selector (radio behaves like tabs, but is controllable) ----
tab = st.radio(
    "View",
    ["📥 Logs Input", "🔎 AI Analysis"],
    horizontal=True,
    index=0 if ss.active_tab == "logs" else 1,
    key="view_selector",
)

# -------------------- LOGS INPUT VIEW --------------------
if tab == "📥 Logs Input":
    ss.active_tab = "logs"
    st.subheader("Provide your logs")

    mode = st.radio(
        "Select input method",
        ["Paste logs", "Upload file", "Use sample logs"],
        index=2, horizontal=True
    )

    logs_text = ""
    filename_hint = "log"

    if mode == "Paste logs":
        logs_text = st.text_area(
            "Paste Kubernetes logs here", height=300, placeholder="kubectl logs ..."
        )
        filename_hint = "pasted"

    elif mode == "Upload file":
        uploaded = st.file_uploader("Upload a .log or .txt file", type=["log", "txt"])
        if uploaded:
            logs_text = uploaded.read().decode(errors="ignore")
            filename_hint = Path(uploaded.name).stem or "uploaded"
            st.success(f"Loaded file: {uploaded.name}")

    else:  # sample
        sample_path = Path("data/sample_logs/k8s_sample.log")
        if sample_path.exists():
            logs_text = sample_path.read_text()
            filename_hint = "sample_k8s"
            st.info("Loaded sample logs ✅")
        else:
            st.error("Sample file not found at data/sample_logs/k8s_sample.log")

    if st.button("🚀 Run AI Analysis", type="primary"):
        if not logs_text.strip():
            st.warning("Please provide logs before analyzing.")
        else:
            with st.spinner("Analyzing logs with AI..."):
                heur = run_heuristics(logs_text)
                report = summarize_logs(logs_text, heur)

            ss.last_report = report
            ss.last_filename = filename_hint
            ss.last_heuristics = heur

            # programmatically switch to analysis view
            ss.active_tab = "analysis"
            st.rerun()

# -------------------- ANALYSIS VIEW --------------------
else:
    ss.active_tab = "analysis"
    st.subheader("AI Generated Report")

    if not ss.last_report:
        st.info("Run analysis from the Logs Input view above.")
    else:
        st.markdown("#### Heuristic Matches")
        if ss.last_heuristics:
            badges = "".join(badge(h["hint"], h.get("severity", "info")) for h in ss.last_heuristics)
            st.markdown(badges, unsafe_allow_html=True)
        else:
            st.write("No common failure patterns detected.")

        st.markdown("---")
        st.markdown("### 🤖 AI Summary Report")
        st.markdown(ss.last_report)

        ts = datetime.now().strftime("%Y%m%d-%H%M")
        fname = f"{ss.last_filename}-ai-log-analysis-{ts}.md"
        st.download_button(
            label="📥 Download Report (.md)",
            data=ss.last_report,
            file_name=fname,
            mime="text/markdown"
        )

