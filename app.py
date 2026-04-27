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
    <h1 style='text-align: center; color: #2E86C1;'>🩺 ASO Care AI</h1>
    <p style='text-align: center; color: gray;'>
    AI-powered symptom checker for quick health insights
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# ===== INPUT =====
user_input = st.text_area(
    "Describe your symptoms",
    placeholder="e.g. fever, headache, nausea..."
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
        st.warning("Please enter your symptoms first.")
    else:
        symptoms = [user_input.lower()]
        results, score = analyze_symptoms(symptoms)

        st.write("---")
        st.subheader("📊 Analysis Result")

        # ===== RISK BADGE =====
        if score >= 5:
            st.markdown("### 🔴 HIGH RISK")
            st.error("Seek medical attention immediately")
        elif score >= 3:
            st.markdown("### 🟠 MEDIUM RISK")
            st.warning("Monitor your symptoms closely")
        else:
            st.markdown("### 🟢 LOW RISK")
            st.success("Basic care should be enough")

        st.write("---")

        # ===== CARDS STYLE OUTPUT =====
        if results:
            for r in results:
                st.markdown(
                    f"""
                    <div style="
                        background-color: #f5f7fa;
                        padding: 15px;
                        border-radius: 10px;
                        margin-bottom: 10px;
                        border-left: 5px solid #2E86C1;
                    ">
                        <h4>🧾 {r['condition']}</h4>
                        <p><b>💡 Advice:</b> {r['advice']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("No strong match found. Please consult a medical professional.")

# ===== FOOTER =====
st.write("---")
st.caption("⚠️ Educational tool only. Not a replacement for medical advice.")