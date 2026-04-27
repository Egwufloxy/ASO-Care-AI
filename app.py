import streamlit as st
from aso_care_ai.logic import analyze_symptoms

st.set_page_config(page_title="ASO Care AI", page_icon="🩺", layout="centered")

st.title("🩺 ASO Care AI")
st.caption("AI-powered symptom checker (educational use only)")

user_input = st.text_area("Describe your symptoms", placeholder="e.g. I have fever and headache")

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze Symptoms")

with col2:
    clear = st.button("Clear")

if clear:
    st.rerun()

if analyze:
    if not user_input.strip():
        st.warning("Please enter symptoms first.")
    else:
        symptoms = [user_input.lower()]
        results, score = analyze_symptoms(symptoms)

        st.divider()
        st.subheader("🔍 Analysis Result")

        if results:
            for r in results:
                st.success(f"Condition: {r['condition']}")
                st.write(f"💡 Advice: {r['advice']}")
                st.write("---")

            st.subheader("⚠️ Risk Level")

            if score >= 5:
                st.error("HIGH RISK — Seek medical attention immediately")
            elif score >= 3:
                st.warning("MEDIUM RISK — Monitor closely")
            else:
                st.success("LOW RISK — Basic care recommended")

        else:
            st.info("No matching symptoms found. Please consult a doctor.")