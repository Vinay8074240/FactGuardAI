import streamlit as st
from main import run_fact_checker
import time

def run_with_retry(claim):
    for i in range(3): # Try 3 times
        try:
            return run_fact_checker(claim)
        except Exception as e:
            if "RateLimitError" in str(e):
                st.warning(f"Rate limit hit. Retrying in 15 seconds... (Attempt {i+1}/3)")
                time.sleep(15)
            else:
                raise e

st.title("🛡️ FactGuard AI: Agentic Fact-Checker")
st.write("Enter a claim below to have our agents verify it.")

claim = st.text_input("Enter Claim:", "Did NASA find water on Mars recently?")

if st.button("Analyze Claim"):
    with st.spinner("Agents are researching and verifying..."):
        final_report = run_fact_checker(claim)
        st.markdown(f"### Final Report\n{final_report}")