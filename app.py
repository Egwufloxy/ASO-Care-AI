import streamlit as st
from aso_care_ai.logic import analyze_symptoms

st.set_page_config(
    page_title="ASO Care AI",
    page_icon="🩺",
    layout="centered"
)

# Header
st.title("🩺 ASO Care AI")
st.caption("AI-powered symptom checker for educational use only")

st.divider()

# Input section
user_input = st.text_area(
    "Describe your symptoms",
    placeholder="e.g. fever, headache, body pain..."
)

col1, col2 = st.columns(2)

with col1:
    analyze_btn = st.button("Analyze")

with col2:
    clear_btn = st.button("Clear")

if clear_btn:
    st.rerun()

# Result section
if analyze_btn:
    if not user_input.strip():
        st.warning("Please enter your symptoms first.")
    else:
        symptoms = [user_input.lower()]
        results, score = analyze_symptoms(symptoms)

        st.divider()
        st.subheader("🔍 Analysis Result")

        # Severity badge
        if score >= 5:
            st.error("🔴 HIGH RISK")
        elif score >= 3:
            st.warning("🟠 MEDIUM RISK")
        else:
            st.success("🟢 LOW RISK")

        st.write("---")

        # Results cards
        if results:
            for r in results:
                with st.container():
                    st.markdown(
                        f"""
                        ### 🧾 {r['condition']}
                        💡 **Advice:** {r['advice']}
                        ---
                        """
                    )
        else:
            st.info("No strong match found. Please consult a medical professional.")
        
        # Footer note
        st.caption("⚠️ This tool is not a substitute for professional medical advice.")