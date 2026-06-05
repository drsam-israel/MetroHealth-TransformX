import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MetroHealth TransformX",
    page_icon="🏥",
    layout="wide"
)

# Load Data
patients = pd.read_csv("data/patients.csv")
facilities = pd.read_csv("data/facilities.csv")
encounters = pd.read_csv("data/encounters.csv")
observations = pd.read_csv("data/observations.csv")
medications = pd.read_csv("data/medications.csv")

# Title
st.title("🏥 MetroHealth TransformX")

st.subheader(
    "Healthcare Interoperability, Intelligence & AI Platform"
)

st.markdown("---")

# KPI Row
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Patients", len(patients))
col2.metric("Facilities", len(facilities))
col3.metric("Encounters", len(encounters))
col4.metric("Observations", len(observations))
col5.metric("Medications", len(medications))

st.markdown("---")

st.header("MetroHealth Ecosystem Overview")

st.write(
    """
    MetroHealth TransformX demonstrates a connected healthcare ecosystem
    supporting interoperability, clinical intelligence,
    operational intelligence, and responsible AI.
    """
)

st.success("MetroHealth TransformX v1.0 Initialized")

st.markdown("---")

st.markdown(
f"""
<div style='background-color:#020817;
padding:25px;
border-radius:15px;
border-left:6px solid #0EA5E9;'>

<h2 style='color:white; margin-bottom:10px;'>
🏥 MetroHealth TransformX™ v1.0
</h2>

<p style='color:#E2E8F0; font-size:20px;'>
Healthcare Interoperability, Intelligence & AI Platform
</p>

<p style='color:#38BDF8; font-size:18px; font-weight:bold;'>
One Patient • One Record • One Connected Healthcare Ecosystem
</p>

<br>

<p style='color:#CBD5E1;'>
Developed by
</p>

<p style='color:white; font-size:22px; font-weight:bold;'>
Samuel Israel, MD
</p>

<p style='color:#CBD5E1;'>
Master of Information Technology (AI Specialization)
</p>

<p style='color:#94A3B8;'>
Healthcare AI • Clinical Intelligence • Digital Health Transformation • Responsible AI
</p>

<hr style='border:1px solid #1E293B;'>

<div style='display:flex; gap:20px; flex-wrap:wrap;'>

<a href='https://healthcare-ai-portfolio-7sndn76vnkbctvfprsbmkj.streamlit.app/'
target='_blank'
style='background:#0EA5E9;color:white;padding:10px 18px;
text-decoration:none;border-radius:8px;font-weight:bold;'>
🌐 Portfolio
</a>

<a href='https://github.com/drsam-israel'
target='_blank'
style='background:#1E293B;color:white;padding:10px 18px;
text-decoration:none;border-radius:8px;font-weight:bold;'>
💻 GitHub
</a>

<a href='https://www.linkedin.com/in/dr-samuel-israel-90893b228'
target='_blank'
style='background:#2563EB;color:white;padding:10px 18px;
text-decoration:none;border-radius:8px;font-weight:bold;'>
🔗 LinkedIn
</a>

</div>

<br>

<p style='color:#64748B;font-size:13px;'>
Powered by Python • Streamlit • Healthcare Analytics • Interoperability • AI Intelligence
</p>

</div>
""",
unsafe_allow_html=True
)