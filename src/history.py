import pandas as pd
import streamlit as st
from datetime import datetime


def initialize_history():
    if "history" not in st.session_state:
        st.session_state.history = pd.DataFrame(
            columns=[
                "Time",
                "Prediction",
                "Confidence",
                "Risk"
            ]
        )


def add_history(prediction, confidence, risk):
    new_row = pd.DataFrame({
        "Time": [datetime.now().strftime("%H:%M:%S")],
        "Prediction": [prediction],
        "Confidence": [f"{confidence:.2f}%"],
        "Risk": [risk]
    })

    st.session_state.history = pd.concat(
        [st.session_state.history, new_row],
        ignore_index=True
    )