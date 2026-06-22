"""
AI Powered Job Scam Detection Platform
Developer: Kummara Nikhil
"""

import os
import streamlit as st

# Backend Modules
from src.predict import predict_job
from src.explain import explain_prediction
from src.file_handler import extract_text
from src.report_generator import generate_report

# Charts
from src.charts import (
    probability_chart,
    pie_chart,
    confidence_gauge
)

# Configuration
from config import CSS_FILE


# ======================================================
# PAGE CONFIGURATION (MUST BE FIRST)
# ======================================================

st.set_page_config(
    page_title="AI Job Scam Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD CSS
# ======================================================

def load_css():
    if os.path.exists(CSS_FILE):
        with open(CSS_FILE, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ======================================================
# SESSION STATE
# ======================================================

if "sample" not in st.session_state:
    st.session_state.sample = ""

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("🛡 AI Job Scam Detector")

    st.markdown("---")

    st.subheader("📌 About")

    st.write(
        """
This application uses **Machine Learning**
and **Natural Language Processing (NLP)**
to classify job advertisements as:

✅ Genuine

❌ Fake
"""
    )

    st.markdown("---")

    st.subheader("⚙ Technologies")

    st.markdown("""
- 🐍 Python
- 🤖 Machine Learning
- 🧠 NLP
- 📊 Scikit-Learn
- 🌐 Streamlit
- 📈 Plotly
""")

    st.markdown("---")

    st.subheader("🧠 AI Model")

    st.success("Logistic Regression")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.info("""
**Kummara Nikhil**

B.Tech CSE (AI & ML)

AI • ML • Data Science
""")

# ======================================================
# HEADER
# ======================================================

st.title("🛡 AI Powered Job Scam Detection Platform")

st.markdown("""
Analyze any job posting using Artificial Intelligence.

The system predicts whether a job advertisement is **Genuine** or **Fake**
using Machine Learning and Natural Language Processing.

Upload a document or paste the job description below.
""")

st.markdown("---")

# ======================================================
# DASHBOARD CARDS
# ======================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="🤖 Model",
        value="Logistic"
    )

with c2:
    st.metric(
        label="🧠 NLP",
        value="TF-IDF"
    )

with c3:
    st.metric(
        label="📂 Formats",
        value="PDF/DOCX/TXT"
    )

with c4:
    st.metric(
        label="⚡ Status",
        value="Ready"
    )

st.markdown("---")

# ======================================================
# SAMPLE JOB
# ======================================================

if st.button("📋 Load Sample Fake Job"):

    st.session_state.sample = """
URGENT HIRING!!

Work From Home

Earn ₹50,000 Weekly

No Experience Required

WhatsApp HR immediately

Limited Seats

Apply Now
"""

# ======================================================
# INPUT SECTION
# ======================================================

left, right = st.columns([1,1])

with left:

    uploaded_file = st.file_uploader(
        "📂 Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

with right:

    job_text = st.text_area(
        "📄 Paste Job Description",
        value=st.session_state.sample,
        height=320
    )

# ======================================================
# READ FILE
# ======================================================

if uploaded_file is not None:

    extracted_text = extract_text(uploaded_file)

    if extracted_text:

        job_text = extracted_text

        st.success("✅ File uploaded successfully!")

        with st.expander("View Extracted Text"):

            st.write(extracted_text)

    else:

        st.error("Unable to extract text from this file.")

st.markdown("---")
# ======================================================
# ANALYZE BUTTON
# ======================================================

if st.button("🔍 Analyze Job Posting", use_container_width=True):

    if job_text.strip() == "":

        st.warning("⚠ Please enter or upload a job description.")

    else:

        with st.spinner("🤖 AI is analyzing the job posting..."):

            result = predict_job(job_text)

            reasons = explain_prediction(job_text)

        prediction = result["prediction"]
        fake_probability = result["fake_probability"]
        real_probability = result["real_probability"]

        confidence = max(
            fake_probability,
            real_probability
        )

        # ===============================================
        # PREDICTION RESULT
        # ===============================================

        st.markdown("---")

        st.header("📊 Prediction Result")

        if prediction == 1:

            prediction_text = "🚨 Fake Job Posting"

            st.error(prediction_text)

        else:

            prediction_text = "✅ Genuine Job Posting"

            st.success(prediction_text)

        # ===============================================
        # METRICS
        # ===============================================

        m1, m2, m3 = st.columns(3)

        with m1:

            st.metric(
                "🟢 Genuine",
                f"{real_probability:.2f}%"
            )

        with m2:

            st.metric(
                "🔴 Fake",
                f"{fake_probability:.2f}%"
            )

        with m3:

            st.metric(
                "🎯 Confidence",
                f"{confidence:.2f}%"
            )

        st.progress(confidence / 100)

        # ===============================================
        # CHARTS
        # ===============================================

        st.markdown("---")

        st.header("📈 AI Prediction Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:

            st.plotly_chart(

                probability_chart(
                    fake_probability,
                    real_probability
                ),

                use_container_width=True

            )

        with chart2:

            st.plotly_chart(

                pie_chart(
                    fake_probability,
                    real_probability
                ),

                use_container_width=True

            )

        st.markdown("---")

        st.subheader("🎯 Model Confidence")

        st.plotly_chart(

            confidence_gauge(confidence),

            use_container_width=True

        )

        # ===============================================
        # AI EXPLANATION
        # ===============================================

        st.markdown("---")

        st.header("🧠 AI Explanation")

        if len(reasons) == 0:

            st.success(
                "No suspicious keywords were detected."
            )

        else:

            st.warning(
                "The following suspicious indicators were detected:"
            )

            for i, reason in enumerate(reasons, start=1):

                st.write(
                    f"**{i}.** {reason}"
                )

        # ===============================================
        # RISK LEVEL
        # ===============================================

        st.markdown("---")

        st.header("⚠ Risk Assessment")

        risk_score = len(reasons)

        if risk_score >= 5:

            risk_level = "HIGH"

            st.error(
                "🔴 HIGH RISK"
            )

        elif risk_score >= 3:

            risk_level = "MEDIUM"

            st.warning(
                "🟠 MEDIUM RISK"
            )

        elif risk_score >= 1:

            risk_level = "LOW"

            st.info(
                "🟡 LOW RISK"
            )

        else:

            risk_level = "SAFE"

            st.success(
                "🟢 SAFE"
            )

        st.markdown("---")
        # ===============================================
        # PDF REPORT
        # ===============================================

        st.markdown("---")

        st.header("📄 Generate AI Report")

        if st.button(
            "📥 Generate PDF Report",
            use_container_width=True
        ):

            report_path = generate_report(
                job_text=job_text,
                prediction=prediction_text,
                confidence=confidence,
                risk=risk_level,
                reasons=reasons
            )

            st.success("✅ Report generated successfully!")

            with open(report_path, "rb") as pdf_file:

                st.download_button(
                    label="⬇ Download PDF Report",
                    data=pdf_file.read(),
                    file_name=report_path.name,
                    mime="application/pdf",
                    use_container_width=True
                )

        # ===============================================
        # JOB SAFETY TIPS
        # ===============================================

        st.markdown("---")

        st.header("💡 Tips to Identify Fake Job Posts")

        tips = [
            "Never pay registration or interview fees.",
            "Verify the company through its official website.",
            "Avoid communication only through WhatsApp or Telegram.",
            "Be cautious of unrealistically high salaries.",
            "Check the recruiter’s official email address.",
            "Research company reviews on LinkedIn or Glassdoor.",
            "Avoid offers demanding immediate joining without interviews.",
            "Read the complete job description before applying."
        ]

        for tip in tips:

            st.info(f"✔ {tip}")

        # ===============================================
        # ANALYZE AGAIN
        # ===============================================

        st.markdown("---")

        if st.button(
            "🔄 Analyze Another Job",
            use_container_width=True
        ):

            st.session_state.sample = ""

            st.rerun()

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

left, center, right = st.columns(3)

with left:

    st.caption("👨‍💻 Developed by")

    st.write("**Kummara Nikhil**")

with center:

    st.caption("🧠 Technologies")

    st.write("Python • NLP • ML • Streamlit")

with right:

    st.caption("🎓 Project")

    st.write("AI Powered Job Scam Detection")

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;padding:15px;">

### 🛡 AI Powered Job Scam Detection Platform

Built using **Machine Learning**, **Natural Language Processing**, and **Streamlit**

⭐ Thank you for using this application.

</div>
""",
unsafe_allow_html=True
)