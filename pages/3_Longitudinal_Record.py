import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Longitudinal Patient Record",
    page_icon="📋",
    layout="wide"
)

patients = pd.read_csv("data/patients.csv")
encounters = pd.read_csv("data/encounters.csv")
facilities = pd.read_csv("data/facilities.csv")
medications = pd.read_csv("data/medications.csv")

st.title("📋 Longitudinal Patient Record")

st.markdown(
"""
One Patient • One Record • One Connected Healthcare Ecosystem
"""
)

st.markdown("---")

selected_patient = st.selectbox(
    "Select Patient",
    patients["patient_id"]
)

patient = patients[
    patients["patient_id"] == selected_patient
].iloc[0]

st.subheader("Patient Information")

col1, col2, col3 = st.columns(3)

col1.metric("Patient ID", patient["patient_id"])
col2.metric("Age", patient["age"])
col3.metric("Gender", patient["gender"])

st.write(f"**Name:** {patient['name']}")
st.write(f"**City:** {patient['city']}")

st.markdown("---")

st.subheader("Healthcare Journey Timeline")

patient_encounters = encounters[
    encounters["patient_id"] == selected_patient
].copy()

patient_encounters = patient_encounters.merge(
    facilities,
    on="facility_id",
    how="left"
)

patient_encounters["date"] = pd.to_datetime(
    patient_encounters["date"]
)

patient_encounters = patient_encounters.sort_values(
    "date"
)

for _, row in patient_encounters.iterrows():

    st.info(
        f"""
        {row['date']}

        **{row['event']}**

        Facility: {row['facility_name']}

        Status: {row['status']}
        """
    )

st.markdown("---")

st.subheader("Medications")

patient_meds = medications[
    medications["patient_id"] == selected_patient
]

st.dataframe(patient_meds, use_container_width=True)