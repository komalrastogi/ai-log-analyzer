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
ss.setdefault("chosen_sample", "Kubernetes Basic")

# --- helper: colored badge HTML ---
def badge(text: str, sev: str) -> str:
    colors = {"error": "#B91C1C", "warning": "#D97706", "info": "#15803D"}
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

    else:  # ---------- CARD-STYLE SAMPLE CHOOSER ----------
        samples = {
            "Kubernetes Basic": {
                "path": Path("data/sample_logs/k8s_sample.log"),
                "desc": "Mix of ImagePullBackOff, CrashLoopBackOff, OOMKilled, and 5xx.",
                "key": "sample_k8s",
            },
            "Probe/DNS Issues": {
                "path": Path("data/sample_logs/k8s_probe_dns.log"),
                "desc": "Liveness/Readiness probe failures, DNSConfigForming, mount perms, OOM.",
                "key": "sample_probe_dns",
            },
            "Ingress/Nginx 5xx": {
                "path": Path("data/sample_logs/nginx_5xx.log"),
                "desc": "Ingress 502/504 with upstream timeouts + probe failure + OOM.",
                "key": "sample_nginx",
            },
        }

        st.write("#### Choose a sample")
        c1, c2, c3 = st.columns(3)

        def card(col, title):
            item = samples[title]
            ok = item["path"].exists()
            with col:
                st.markdown(
                    f"""
                    <div style="border:1px solid #374151;border-radius:12px;padding:12px;height:164px">
                      <div style="font-weight:600;margin-bottom:6px">{title}</div>
                      <div style="font-size:13px;opacity:0.85;margin-bottom:10px">{item['desc']}</div>
                      <div>{"✅ Ready" if ok else "❌ Missing file"}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button(
                    f"Use {item['key'].replace('_',' ').title()}",
                    key=f"use_{item['key']}",
                    disabled=not ok,
                    on_click=lambda: ss.update(chosen_sample=title),
                )

        card(c1, "Kubernetes Basic")
        card(c2, "Probe/DNS Issues")
        card(c3, "Ingress/Nginx 5xx")

        chosen = ss.get("chosen_sample", "Kubernetes Basic")
        item = samples[chosen]
        if item["path"].exists():
            logs_text = item["path"].read_text()
            filename_hint = item["key"]
            st.success(f"Loaded sample: {chosen} ✅")
        else:
            st.error(f"Sample file not found: {item['path']}")

    # ----- Run analysis -----
    if st.button("🚀 Run AI Analysis", type="primary"):
        if not logs_text.strip():
            st.warning("Please provide logs before analyzing.")
        else:
            try:
                with st.spinner("Analyzing logs with AI..."):
                    heur = run_heuristics(logs_text)
                    report = summarize_logs(logs_text, heur)
                ss.last_report = report
                ss.last_filename = filename_hint
                ss.last_heuristics = heur
                ss.active_tab = "analysis"   # programmatic switch
                st.rerun()
            except Exception as e:
                st.error(f"Analysis failed: {e}")

# -------------------- ANALYSIS VIEW --------------------
else:
    ss.active_tab = "analysis"
    st.subheader("AI Generated Report")
    if not ss.last_report:
        st.info("Run analysis from the Logs Input view above.")
    else:
        st.markdown("#### Heuristic Matches")
        if ss.last_heuristics:
            badges_html = "".join(badge(h["hint"], h.get("severity", "info")) for h in ss.last_heuristics)
            st.markdown(badges_html, unsafe_allow_html=True)
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
            mime="text/markdown",
        )

