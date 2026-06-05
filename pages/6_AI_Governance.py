import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Governance",
    page_icon="🛡️",
    layout="wide"
)

patients = pd.read_csv("data/patients.csv")
observations = pd.read_csv("data/observations.csv")

st.title("🛡️ Responsible AI Governance")
st.subheader("Model Transparency, Risk Controls & Clinical AI Oversight")

st.markdown("---")

# Simulated governance metrics
model_metrics = pd.DataFrame({
    "Model": [
        "Sepsis Early Warning",
        "Readmission Risk",
        "Capacity Forecasting",
        "Clinical Triage Assistant"
    ],
    "Accuracy": [0.90, 0.84, 0.88, 0.81],
    "Explainability": [0.92, 0.89, 0.86, 0.78],
    "Drift Risk": ["Low", "Moderate", "Low", "Moderate"],
    "Governance Status": ["Approved", "Approved", "Approved", "Review Required"]
})

col1, col2, col3, col4 = st.columns(4)
col1.metric("AI Models", len(model_metrics))
col2.metric("Approved Models", len(model_metrics[model_metrics["Governance Status"] == "Approved"]))
col3.metric("Models in Review", len(model_metrics[model_metrics["Governance Status"] == "Review Required"]))
col4.metric("Average Explainability", f"{model_metrics['Explainability'].mean():.2f}")

st.markdown("---")

st.subheader("AI Model Governance Register")
st.dataframe(model_metrics, use_container_width=True)

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Model Performance")
    fig = px.bar(
        model_metrics,
        x="Model",
        y="Accuracy"
    )
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Explainability Score")
    fig = px.bar(
        model_metrics,
        x="Model",
        y="Explainability"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Governance Controls")

controls = pd.DataFrame({
    "Control Domain": [
        "Data Quality",
        "Clinical Validation",
        "Bias Monitoring",
        "Explainability",
        "Human Oversight",
        "Model Drift Monitoring",
        "Audit Logging",
        "Security & Privacy"
    ],
    "Status": [
        "Implemented",
        "In Progress",
        "Implemented",
        "Implemented",
        "Implemented",
        "In Progress",
        "Implemented",
        "Implemented"
    ]
})

st.dataframe(controls, use_container_width=True)

st.markdown("---")

st.warning(
    """
    Responsible AI Principle:

    MetroHealth TransformX does not replace clinicians.
    It augments clinical decision-making through explainable,
    governed, and human-supervised intelligence.
    """
)

st.success("Responsible AI Governance module operational.")