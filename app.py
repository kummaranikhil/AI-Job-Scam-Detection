import streamlit as st
from pathlib import Path

from src.predict import predict_job
from src.explain import explain_prediction
from src.file_handler import extract_text
from src.charts import probability_chart, pie_chart, confidence_gauge
from src.report_generator import generate_report

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Job Scam Detection Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CUSTOM CSS
# ==========================================================

def load_css():
    css_path = Path("assets/style.css")

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================================================
# SESSION STATE
# ==========================================================

if "sample" not in st.session_state:
    st.session_state.sample = ""

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🛡️ AI Job Scam Detector")

    st.markdown("---")

    st.subheader("📌 About")

    st.info("""
This AI application detects fraudulent job postings using

• Machine Learning

• Natural Language Processing

• Explainable AI

• TF-IDF Vectorization
""")

    st.markdown("---")

    st.subheader("🛠 Technologies")

    st.success("""
✅ Python

✅ Streamlit

✅ Scikit-Learn

✅ Pandas

✅ TF-IDF

✅ Plotly

✅ ReportLab
""")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.success("""
Kummara Nikhil

B.Tech CSE (AI & ML)
""")

    st.markdown("---")

    st.caption("Version 2.0")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class='main-title'>
🛡️ AI Job Scam Detection Platform
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Detect Fraudulent Job Postings using Machine Learning, NLP & Explainable AI
</div>
""", unsafe_allow_html=True)

# ==========================================================
# FEATURE CARDS
# ==========================================================

card1, card2, card3 = st.columns(3)

with card1:
    st.info("""
### 🤖 AI Engine

✔ TF-IDF

✔ Logistic Regression

✔ Explainable AI
""")

with card2:
    st.info("""
### 📂 Supported Files

✔ PDF

✔ DOCX

✔ TXT
""")

with card3:
    st.info("""
### 📊 Features

✔ Charts

✔ PDF Report

✔ Risk Analysis
""")

st.markdown("---")

# ==========================================================
# SAMPLE BUTTON
# ==========================================================

if st.button("📋 Load Sample Fake Job"):

    st.session_state.sample = """
URGENT HIRING!!

Work From Home

Earn ₹50,000 Weekly

No Experience Required

WhatsApp HR Immediately

Limited Seats

Apply Now
"""

# ==========================================================
# MAIN LAYOUT
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.subheader("📄 Job Description")

    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT",
        type=["pdf", "docx", "txt"]
    )

    job_text = st.text_area(
        "Paste Job Description",
        value=st.session_state.sample,
        height=350
    )

    if uploaded_file is not None:

        extracted_text = extract_text(uploaded_file)

        if extracted_text:

            job_text = extracted_text

            st.success("✅ File uploaded successfully.")

            with st.expander("View Extracted Text"):

                st.write(extracted_text)

        else:

            st.error("Unable to read uploaded file.")

    analyze = st.button(
        "🔍 Analyze Job Posting",
        use_container_width=True
    )

with right:

    st.subheader("ℹ️ Instructions")

    st.info("""
1. Upload a PDF, DOCX or TXT file

OR

2. Paste the job description

3. Click Analyze

The AI will predict whether the job posting is Genuine or Fake.
""")

    st.warning("""
⚠ Never share personal information with unknown recruiters.

Always verify the company before applying.
""")

# ==========================================================
# PREDICTION STARTS HERE
# ==========================================================

if analyze:

    if job_text.strip() == "":

        st.warning("Please upload or enter a job description.")

    else:

        with st.spinner("Analyzing Job Posting..."):

            try:

                result = predict_job(job_text)

                reasons = explain_prediction(job_text)

            except Exception as e:

                st.error("❌ Something went wrong while analyzing the job posting.")

                st.exception(e)

                st.stop()
            prediction = result["prediction"]

            fake_probability = result["fake_probability"]

            real_probability = result["real_probability"]

            confidence = max(
                fake_probability,
                real_probability
            )
        # ==========================================================
        # PREDICTION RESULT
        # ==========================================================

        st.markdown("---")

        st.header("📊 Prediction Result")

        if prediction == 1:

            prediction_text = "🚨 Fake Job Posting"

            st.error(prediction_text)

        else:

            prediction_text = "✅ Genuine Job Posting"

            st.success(prediction_text)

        # ==========================================================
        # PROBABILITY
        # ==========================================================

        st.markdown("---")

        st.header("📈 Prediction Probability")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🟢 Genuine",
                f"{real_probability:.2f}%"
            )

        with col2:

            st.metric(
                "🔴 Fake",
                f"{fake_probability:.2f}%"
            )

        st.progress(confidence / 100)

        st.success(
            f"Model Confidence : {confidence:.2f}%"
        )

        # ==========================================================
        # VISUAL ANALYTICS
        # ==========================================================

        st.markdown("---")

        st.header("📊 AI Visual Analytics")

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

        st.plotly_chart(

            confidence_gauge(confidence),

            use_container_width=True

        )

        # ==========================================================
        # AI EXPLANATION
        # ==========================================================

        st.markdown("---")

        st.header("🔍 Explainable AI")

        if len(reasons) == 0:

            st.success(
                "✅ No suspicious keywords detected."
            )

        else:

            st.warning(
                "The following suspicious indicators were found:"
            )

            for reason in reasons:

                st.write("•", reason)

        # ==========================================================
        # RISK ANALYSIS
        # ==========================================================

        st.markdown("---")

        st.header("⚠ Risk Analysis")

        risk = len(reasons)

        if risk >= 5:

            risk_level = "HIGH"

            st.error("🔴 HIGH RISK")

        elif risk >= 3:

            risk_level = "MEDIUM"

            st.warning("🟠 MEDIUM RISK")

        elif risk >= 1:

            risk_level = "LOW"

            st.info("🟡 LOW RISK")

        else:

            risk_level = "SAFE"

            st.success("🟢 SAFE")

        st.markdown("---")
        # ==========================================================
        # PDF REPORT GENERATION
        # ==========================================================

        st.header("📄 Analysis Report")

        if st.button("📥 Generate PDF Report"):

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
                    data=pdf_file,
                    file_name=report_path.name,
                    mime="application/pdf"
                )

        # ==========================================================
        # ANALYSIS SUMMARY
        # ==========================================================

        st.markdown("---")

        st.header("📋 Analysis Summary")

        summary_col1, summary_col2 = st.columns(2)

        with summary_col1:

            st.metric(
                "Prediction",
                "Fake Job" if prediction == 1 else "Genuine Job"
            )

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        with summary_col2:

            st.metric(
                "Risk Level",
                risk_level
            )

            st.metric(
                "Suspicious Indicators",
                len(reasons)
            )

        # ==========================================================
        # JOB DESCRIPTION PREVIEW
        # ==========================================================

        st.markdown("---")

        st.header("📄 Submitted Job Description")

        with st.expander("View Job Description"):

            st.write(job_text)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; padding:20px;'>

    <h3>🛡️ AI Job Scam Detection Platform</h3>

    <p>
    Built using <b>Python</b>,
    <b>Machine Learning</b>,
    <b>Natural Language Processing</b>,
    <b>Streamlit</b>,
    <b>Plotly</b>,
    and <b>Scikit-Learn</b>.
    </p>

    <hr>

    <p>
    👨‍💻 Developed by <b>Kummara Nikhil</b><br>
    B.Tech CSE (AI & ML)
    </p>

    </div>
    """,
    unsafe_allow_html=True
)