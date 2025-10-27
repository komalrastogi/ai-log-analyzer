# app/ai_summary.py
import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an SRE/DevOps assistant.
Input: Kubernetes logs + heuristic hints.
Output: concise markdown with:
1. Summary
2. Root Cause (probable)
3. Recommended Fix (exact steps/kubectl if possible)
4. Next Steps
Format clearly with bullet points.
"""

def summarize_logs(log_text: str, heuristics: List[Dict]) -> str:
    """
    Summarize logs using OpenAI GPT model
    """
    hints = "\n".join([f"- {h['hint']}" for h in heuristics]) or "- None"
    user_prompt = f"""Logs:
'''
{log_text[:20000]}
'''
Heuristic Hints:
{hints}

Create the markdown summary now.
"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )
    return resp.choices[0].message.content
