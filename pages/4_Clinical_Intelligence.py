import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Clinical Intelligence",
    page_icon="🧠",
    layout="wide"
)

patients = pd.read_csv("data/patients.csv")
observations = pd.read_csv("data/observations.csv")

st.title("🧠 Clinical Intelligence")
st.subheader("Sepsis Risk, Abnormal Labs & Early Warning Signals")

st.markdown("---")

# Risk rules
risk_obs = observations.copy()

risk_obs["risk_flag"] = False

risk_obs.loc[
    ((risk_obs["test_name"] == "Lactate") & (risk_obs["result"] >= 4)) |
    ((risk_obs["test_name"] == "WBC") & (risk_obs["result"] >= 15)) |
    ((risk_obs["test_name"] == "Temperature") & (risk_obs["result"] >= 38.5)) |
    ((risk_obs["test_name"] == "Oxygen Saturation") & (risk_obs["result"] <= 90)),
    "risk_flag"
] = True

high_risk = risk_obs[risk_obs["risk_flag"] == True]

# ==========================
# Sepsis Risk Scoring
# ==========================

risk_scores = []

for patient_id in observations["patient_id"].unique():

    patient_obs = observations[
        observations["patient_id"] == patient_id
    ]

    score = 0

    if ((patient_obs["test_name"] == "Lactate") &
        (patient_obs["result"] >= 4)).any():
        score += 30

    if ((patient_obs["test_name"] == "WBC") &
        (patient_obs["result"] >= 15)).any():
        score += 25

    if ((patient_obs["test_name"] == "Temperature") &
        (patient_obs["result"] >= 38.5)).any():
        score += 20

    if ((patient_obs["test_name"] == "Oxygen Saturation") &
        (patient_obs["result"] <= 90)).any():
        score += 25

    risk_scores.append(
        {
            "patient_id": patient_id,
            "risk_score": score
        }
    )

risk_df = pd.DataFrame(risk_scores)

risk_df["risk_level"] = "Low"

risk_df.loc[
    risk_df["risk_score"] >= 25,
    "risk_level"
] = "Moderate"

risk_df.loc[
    risk_df["risk_score"] >= 50,
    "risk_level"
] = "High"

risk_df.loc[
    risk_df["risk_score"] >= 75,
    "risk_level"
] = "Critical"

st.markdown("---")

st.subheader("Sepsis Risk Stratification")

risk_summary = (
    risk_df["risk_level"]
    .value_counts()
    .reset_index()
)

risk_summary.columns = ["Risk Level", "Patients"]

import plotly.express as px

fig = px.pie(
    risk_summary,
    names="Risk Level",
    values="Patients",
    hole=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("Top High-Risk Patients")

high_risk_patients = risk_df.merge(
    patients,
    on="patient_id",
    how="left"
)

high_risk_patients = high_risk_patients.sort_values(
    "risk_score",
    ascending=False
)

st.dataframe(
    high_risk_patients.head(25),
    use_container_width=True
)

critical_count = len(
    risk_df[
        risk_df["risk_level"] == "Critical"
    ]
)

high_count = len(
    risk_df[
        risk_df["risk_level"] == "High"
    ]
)

st.error(
    f"""
    🚨 Clinical Early Warning Summary

    Critical Risk Patients: {critical_count}

    High Risk Patients: {high_count}

    Review recommended for priority clinical intervention.
    """
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Observations", len(observations))
col2.metric("Abnormal Signals", len(high_risk))
col3.metric("High-Risk Patients", high_risk["patient_id"].nunique())

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Abnormal Signals by Test")
    chart_data = high_risk["test_name"].value_counts().reset_index()
    chart_data.columns = ["Test", "Count"]
    fig = px.bar(chart_data, x="Test", y="Count")
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Clinical Observation Distribution")
    selected_test = st.selectbox(
        "Select Test",
        sorted(observations["test_name"].unique())
    )
    test_data = observations[observations["test_name"] == selected_test]
    fig = px.histogram(test_data, x="result")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("High-Risk Clinical Signals")

high_risk_display = high_risk.merge(
    patients[["patient_id", "name", "age", "gender", "city"]],
    on="patient_id",
    how="left"
)

st.dataframe(
    high_risk_display[
        ["patient_id", "name", "age", "gender", "city", "test_name", "result"]
    ],
    use_container_width=True
)

st.success("Clinical Intelligence module operational.")