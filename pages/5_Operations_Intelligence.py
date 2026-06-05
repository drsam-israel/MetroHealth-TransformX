import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Operations Intelligence",
    page_icon="📊",
    layout="wide"
)

encounters = pd.read_csv("data/encounters.csv")
facilities = pd.read_csv("data/facilities.csv")
patients = pd.read_csv("data/patients.csv")

encounters["date"] = pd.to_datetime(encounters["date"])

ops = encounters.merge(facilities, on="facility_id", how="left")

st.title("📊 Operations Intelligence")
st.subheader("Facility Utilization, Patient Flow & Capacity Signals")

st.markdown("---")

active_encounters = len(ops[ops["status"] == "Active"])
pending_encounters = len(ops[ops["status"] == "Pending"])
completed_encounters = len(ops[ops["status"] == "Completed"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Encounters", len(ops))
col2.metric("Active Encounters", active_encounters)
col3.metric("Pending Encounters", pending_encounters)
col4.metric("Completed Encounters", completed_encounters)

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Encounter Volume by Facility")
    facility_volume = (
        ops["facility_name"]
        .value_counts()
        .reset_index()
    )
    facility_volume.columns = ["Facility", "Encounters"]
    fig = px.bar(facility_volume, x="Facility", y="Encounters")
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Encounter Status Distribution")
    status_counts = (
        ops["status"]
        .value_counts()
        .reset_index()
    )
    status_counts.columns = ["Status", "Count"]
    fig = px.pie(status_counts, names="Status", values="Count", hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Patient Flow Trend")

daily_flow = (
    ops.groupby(ops["date"].dt.date)
    .size()
    .reset_index(name="Encounters")
)

fig = px.line(daily_flow, x="date", y="Encounters")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Capacity Pressure Index")

capacity = (
    ops.groupby("facility_name")
    .size()
    .reset_index(name="Encounter Volume")
)

capacity["Capacity Pressure"] = pd.cut(
    capacity["Encounter Volume"],
    bins=[0, 100, 180, 1000],
    labels=["Low", "Moderate", "High"]
)

st.dataframe(capacity, use_container_width=True)

st.success("Operations Intelligence module operational.")