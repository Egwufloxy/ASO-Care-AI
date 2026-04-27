import streamlit as st
from aso_care_ai.logic import analyze_symptoms

st.set_page_config(
    page_title="ASO Care AI",
    page_icon="🩺",
    layout="centered"
)

# ===== HEADER =====
st.markdown(
    """
    <div style='text-align:center;'>
        <h1>🩺 ASO Care AI</h1>
        <p style='color:gray;'>Smart AI-powered symptom checker</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

# ===== INPUT =====
user_input = st.text_area(
    "Enter your symptoms",
    placeholder="e.g. fever, headache, body pain..."
)

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("🔍 Analyze")

with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.rerun()

# ===== RESULTS =====
if analyze:
    if not user_input.strip():
        st.warning("Please enter symptoms first.")
    else:
        symptoms = [user_input.lower()]
        results, score = analyze_symptoms(symptoms)

        st.write("---")
        st.subheader("📊 Result")

        # Risk display
        if score >= 5:
            st.error("🔴 HIGH RISK")
        elif score >= 3:
            st.warning("🟠 MEDIUM RISK")
        else:
            st.success("🟢 LOW RISK")

        st.write("---")

        # Result cards
        if results:
            for r in results:
                st.markdown(
                    f"""
                    <div style="
                        padding:15px;
                        border-radius:10px;
                        background-color:#f4f6f7;
                        border-left:5px solid #3498db;
                        margin-bottom:10px;
                    ">
                        <h4>🧾 {r['condition']}</h4>
                        <p><b>💡 Advice:</b> {r['advice']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("No match found. Please consult a doctor.")

# ===== FOOTER =====
st.write("---")
st.caption("⚠️ Educational tool only. Not medical advice.")