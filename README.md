
🛡 AI-Powered Job Scam Detection Platform

Machine Learning • NLP • Streamlit • Scikit-Learn

Detect Fraudulent Job Postings Using Artificial Intelligence



# 🛡️ AI-Powered Job Scam Detection Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered web application...

An AI-powered web application that detects fraudulent job postings using **Machine Learning** and **Natural Language Processing (NLP)**. The application analyzes job descriptions and predicts whether a posting is **Genuine** or **Fraudulent**, helping job seekers identify potential scams before applying.

## 🌐 Live Demo

**Live Application:**
https://ai-job-scam-detection-sjappxmxsrjtqvh9amhvcr.streamlit.app/

## 📂 GitHub Repository

https://github.com/kummaranikhil/AI-Job-Scam-Detection

---

# 📖 Project Overview

Online job scams have become increasingly common, with fake recruiters posting misleading job advertisements to collect money or personal information from applicants.

This project uses Machine Learning and Natural Language Processing to analyze job descriptions and classify them as either:

* ✅ Genuine Job Posting
* 🚨 Fraudulent Job Posting

The application provides prediction probabilities, confidence scores, visual analytics, and suspicious keyword detection through an interactive Streamlit dashboard.

---

# ✨ Features

* 🤖 AI-powered job scam detection
* 🧠 Natural Language Processing (NLP)
* 📄 Supports PDF, DOCX, and TXT file uploads
* 📝 Manual job description input
* 📊 Interactive Plotly visualizations
* 📈 Prediction confidence gauge
* 🚨 Risk assessment based on suspicious keywords
* 🔍 Explainable AI indicators
* 🌐 Fully deployed on Streamlit Community Cloud

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorization

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Web Framework

* Streamlit

### Document Processing

* pdfplumber
* python-docx
* ReportLab

---

# 🧠 Machine Learning Workflow

```
Job Description
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Logistic Regression Model
        │
        ▼
Prediction
        │
        ▼
Probability + Confidence + Risk Analysis
```

---

# 📂 Project Structure

```
AI-Job-Scam-Detection/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── models/
│   ├── job_scam_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── feature_columns.pkl
│
├── src/
│   ├── predict.py
│   ├── preprocessing.py
│   ├── explain.py
│   ├── charts.py
│   ├── file_handler.py
│   ├── logger.py
│   └── report_generator.py
```

---

# 📊 Dataset

**Source:** Kaggle

**Dataset:** Fake Job Postings Dataset

The dataset contains real and fraudulent job advertisements with textual information such as:

* Job Title
* Company Profile
* Job Description
* Requirements
* Benefits
* Employment Type
* Industry
* Fraudulent Label

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/kummaranikhil/AI-Job-Scam-Detection.git
```

Move into the project folder

```bash
cd AI-Job-Scam-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

### 🏠 Home Page

> *(Add a screenshot here)*

### 🚨 Fake Job Prediction

> *(Add a screenshot here)*

### 📊 Analytics Dashboard

> *(Add a screenshot here)*

### 📈 Confidence Visualization

> *(Add a screenshot here)*

---

# 🔮 Future Improvements

* Deep Learning (BERT / DistilBERT)
* Explainable AI using SHAP
* Company website verification
* Email domain validation
* URL reputation analysis
* Dark Mode
* User authentication
* Admin dashboard with analytics
* REST API integration

---

# 👨‍💻 Developer

**Kummara Nikhil**

B.Tech – Computer Science Engineering (AI & ML)

Aspiring AI Engineer | Machine Learning | Data Science | NLP

GitHub:
https://github.com/kummaranikhil

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

It helps support the project and encourages future development.

---

# 📜 License

This project is developed for educational and portfolio purposes.
