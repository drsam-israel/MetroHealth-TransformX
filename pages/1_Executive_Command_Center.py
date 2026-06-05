import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Executive Command Center",
    page_icon="📊",
    layout="wide"
)

# =========================
# Load Data
# =========================
patients = pd.read_csv("data/patients.csv")
facilities = pd.read_csv("data/facilities.csv")
encounters = pd.read_csv("data/encounters.csv")
observations = pd.read_csv("data/observations.csv")
medications = pd.read_csv("data/medications.csv")

encounters["date"] = pd.to_datetime(encounters["date"])

ecosystem = encounters.merge(
    facilities,
    on="facility_id",
    how="left"
)

# =========================
# Header
# =========================
st.title("📊 Executive Command Center")

st.subheader("Real-Time Healthcare Ecosystem Intelligence")

st.markdown(
    """
    **One Patient • One Record • One Connected Healthcare Ecosystem**

    Executive visibility across connected facilities, patient journeys,
    clinical activity, operational utilization, and AI-enabled healthcare intelligence.
    """
)

st.markdown("---")

# =========================
# KPI Cards
# =========================
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Patients", f"{len(patients):,}")
col2.metric("Facilities", f"{len(facilities):,}")
col3.metric("Encounters", f"{len(encounters):,}")
col4.metric("Observations", f"{len(observations):,}")
col5.metric("Medications", f"{len(medications):,}")

st.markdown("---")

# =========================
# Executive Summary
# =========================
active_count = len(encounters[encounters["status"] == "Active"])
pending_count = len(encounters[encounters["status"] == "Pending"])
completed_count = len(encounters[encounters["status"] == "Completed"])

# =========================
# Dynamic Executive Intelligence Summary
# =========================

# High-risk clinical indicators
risk_obs = observations.copy()

risk_obs["risk_flag"] = False

risk_obs.loc[
    ((risk_obs["test_name"] == "Lactate") & (risk_obs["result"] >= 4)) |
    ((risk_obs["test_name"] == "WBC") & (risk_obs["result"] >= 15)) |
    ((risk_obs["test_name"] == "Temperature") & (risk_obs["result"] >= 38.5)) |
    ((risk_obs["test_name"] == "Oxygen Saturation") & (risk_obs["result"] <= 90)),
    "risk_flag"
] = True

high_risk_patients = risk_obs[risk_obs["risk_flag"] == True]["patient_id"].nunique()

# Active encounters
active_count = len(encounters[encounters["status"] == "Active"])
pending_count = len(encounters[encounters["status"] == "Pending"])
completed_count = len(encounters[encounters["status"] == "Completed"])

# Highest activity encounter type
top_event = encounters["event"].value_counts().idxmax()
top_event_count = encounters["event"].value_counts().max()

# Highest activity facility type
top_facility_type = ecosystem["facility_type"].value_counts().idxmax()
top_facility_type_count = ecosystem["facility_type"].value_counts().max()

st.markdown("### Executive Intelligence Summary")

st.markdown(
    f"""
    • **{len(patients):,} patients** are currently connected across **{len(facilities):,} healthcare facilities**.

    • **{active_count:,} active encounters** require ongoing operational oversight.

    • **{high_risk_patients:,} patients** exhibit one or more high-risk clinical indicators.

    • **{top_event}** is the highest-volume encounter type with **{top_event_count:,} events**.

    • **{top_facility_type}** facilities account for the highest activity volume with **{top_facility_type_count:,} encounters**.

    • Current network status: **Operational**.
    """
)

st.markdown("---")

# =========================
# Operational KPIs
# =========================
colA, colB, colC = st.columns(3)

colA.metric("Active Encounters", f"{active_count:,}")
colB.metric("Pending Encounters", f"{pending_count:,}")
colC.metric("Completed Encounters", f"{completed_count:,}")

st.markdown("---")

# =========================
# Charts Row 1
# =========================
left, right = st.columns(2)

with left:
    st.subheader("Encounter Volume by Facility")

    facility_volume = (
        ecosystem["facility_name"]
        .value_counts()
        .reset_index()
    )
    facility_volume.columns = ["Facility", "Encounters"]

    fig = px.bar(
        facility_volume,
        x="Facility",
        y="Encounters",
        text="Encounters"
    )
    fig.update_layout(
        xaxis_title="Facility",
        yaxis_title="Encounters",
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Facility Network Composition")

    facility_counts = (
        facilities["facility_type"]
        .value_counts()
        .reset_index()
    )
    facility_counts.columns = ["Facility Type", "Count"]

    fig = px.pie(
        facility_counts,
        names="Facility Type",
        values="Count",
        hole=0.45
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# Charts Row 2
# =========================
left, right = st.columns(2)

with left:
    st.subheader("Encounters by Type")

    encounter_counts = (
        encounters["event"]
        .value_counts()
        .reset_index()
    )
    encounter_counts.columns = ["Event", "Count"]

    fig = px.bar(
        encounter_counts,
        x="Event",
        y="Count",
        text="Count"
    )
    fig.update_layout(
        xaxis_title="Encounter Type",
        yaxis_title="Count",
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Encounter Status Distribution")

    status_counts = (
        encounters["status"]
        .value_counts()
        .reset_index()
    )
    status_counts.columns = ["Status", "Count"]

    fig = px.pie(
        status_counts,
        names="Status",
        values="Count",
        hole=0.45
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# Trend
# =========================
st.subheader("Healthcare Activity Trend")

daily_encounters = (
    encounters
    .groupby(encounters["date"].dt.date)
    .size()
    .reset_index(name="Encounters")
)

fig = px.line(
    daily_encounters,
    x="date",
    y="Encounters",
    markers=True
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Daily Encounters"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# Real-Time Feed
# =========================
st.subheader("Real-Time Activity Feed")

latest_events = (
    ecosystem
    .sort_values("date", ascending=False)
    .head(15)
)

latest_events = latest_events[
    [
        "date",
        "patient_id",
        "facility_name",
        "facility_type",
        "event",
        "status"
    ]
]

st.dataframe(latest_events, use_container_width=True)

st.markdown("---")

# =========================
# Platform Status
# =========================
st.success(
    """
    Executive Command Center operational.

    Connected Healthcare Intelligence Environment Active.
    """
)