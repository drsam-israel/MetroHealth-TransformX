import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Patient Registry",
    page_icon="👤",
    layout="wide"
)

patients = pd.read_csv("data/patients.csv")
encounters = pd.read_csv("data/encounters.csv")
medications = pd.read_csv("data/medications.csv")
observations = pd.read_csv("data/observations.csv")

st.title("👤 Patient Registry")
st.subheader("Master Patient Index & Connected Patient Directory")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", len(patients))
col2.metric("Cities Covered", patients["city"].nunique())
col3.metric("Male Patients", len(patients[patients["gender"] == "Male"]))
col4.metric("Female Patients", len(patients[patients["gender"] == "Female"]))

st.markdown("---")

search = st.text_input("Search by Patient ID or Name")

filtered = patients.copy()

if search:
    filtered = filtered[
        filtered["patient_id"].str.contains(search, case=False, na=False)
        | filtered["name"].str.contains(search, case=False, na=False)
    ]

col1, col2 = st.columns(2)

with col1:
    city_filter = st.selectbox(
        "City",
        ["All Cities"] + sorted(patients["city"].unique().tolist())
    )

with col2:
    gender_filter = st.selectbox(
        "Gender",
        ["All Genders"] + sorted(patients["gender"].unique().tolist())
    )

if city_filter != "All Cities":
    filtered = filtered[filtered["city"] == city_filter]

if gender_filter != "All Genders":
    filtered = filtered[filtered["gender"] == gender_filter]

st.markdown("### Patient Directory")
st.dataframe(filtered, use_container_width=True)

st.markdown("---")

st.markdown("### Patient Activity Summary")

summary = encounters.groupby("patient_id").size().reset_index(name="Total Encounters")
summary = summary.merge(patients, on="patient_id", how="left")
summary = summary[["patient_id", "name", "age", "gender", "city", "Total Encounters"]]
summary = summary.sort_values("Total Encounters", ascending=False)

st.dataframe(summary.head(20), use_container_width=True)

st.success("Patient Registry operational.")