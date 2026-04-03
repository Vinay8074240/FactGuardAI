import streamlit as st
from main import run_fact_checker

st.title("🛡️ FactGuard AI: Agentic Fact-Checker")
st.write("Enter a claim below to have our agents verify it.")

claim = st.text_input("Enter Claim:", "Did NASA find water on Mars recently?")

if st.button("Analyze Claim"):
    with st.spinner("Agents are researching and verifying..."):
        final_report = run_fact_checker(claim)
        st.markdown(f"### Final Report\n{final_report}")