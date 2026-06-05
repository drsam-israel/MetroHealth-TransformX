import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HIIAP Interoperability",
    page_icon="🔗",
    layout="wide"
)

patients = pd.read_csv("data/patients.csv")
encounters = pd.read_csv("data/encounters.csv")
observations = pd.read_csv("data/observations.csv")
medications = pd.read_csv("data/medications.csv")
facilities = pd.read_csv("data/facilities.csv")

st.title("🔗 HIIAP Interoperability Layer")
st.subheader("Healthcare Interoperability, Integration & API Platform")

st.markdown(
    """
    **One Patient • Multiple Systems • Unified Record**

    Demonstrating how healthcare data can move across hospitals,
    laboratories, pharmacies, and digital health platforms without replacing existing EHR systems.
    """
)

st.markdown("---")

selected_patient = st.selectbox(
    "Select Patient",
    patients["patient_id"] + " | " + patients["name"]
)

patient_id = selected_patient.split(" | ")[0]
patient = patients[patients["patient_id"] == patient_id].iloc[0]

st.markdown("### Master Patient Index")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Patient ID", patient["patient_id"])
col2.metric("Age", patient["age"])
col3.metric("Gender", patient["gender"])
col4.metric("City", patient["city"])

st.markdown("---")

st.markdown("### Connected Healthcare Events")

enc = encounters[encounters["patient_id"] == patient_id].copy()
enc = enc.merge(facilities, on="facility_id", how="left")
enc["date"] = pd.to_datetime(enc["date"])
enc = enc.sort_values("date")

if enc.empty:
    st.warning("No connected events found for this patient.")
else:
    for _, row in enc.iterrows():
        st.markdown(
            f"""
            <div style='background:#F8FAFC;
            padding:16px;
            border-radius:10px;
            border-left:5px solid #0EA5E9;
            margin-bottom:12px;'>

            <b>{row['event']}</b><br>
            Date: {row['date']}<br>
            Facility: {row['facility_name']}<br>
            Type: {row['facility_type']}<br>
            Status: {row['status']}

            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Clinical Observations")
    obs = observations[observations["patient_id"] == patient_id]
    st.dataframe(obs, use_container_width=True)

with colB:
    st.subheader("Medication History")
    meds = medications[medications["patient_id"] == patient_id]
    st.dataframe(meds, use_container_width=True)

st.markdown("---")

st.info(
    """
    **Interoperability Demonstration**

    Source Systems → HIIAP → Unified Longitudinal Record → Clinical & Executive Intelligence

    This demonstrates the platform’s core value: hospitals can retain their existing systems while participating in a connected healthcare data ecosystem.
    """
)

st.success("HIIAP Interoperability Layer operational.")