import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Transformation Maturity",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Digital Health Transformation Maturity")
st.subheader("MetroHealth TransformX Readiness & Maturity Assessment")

st.markdown(
    """
    **Purpose:** Assess how prepared a healthcare organization is for interoperability,
    intelligence, AI adoption, governance, and enterprise-scale digital transformation.
    """
)

st.markdown("---")

domains = pd.DataFrame({
    "Domain": [
        "Leadership & Strategy",
        "Data Governance",
        "Interoperability",
        "Healthcare Intelligence",
        "Clinical AI",
        "Operations Intelligence",
        "Responsible AI Governance",
        "Workforce Readiness"
    ],
    "Score": [4, 3, 4, 4, 3, 4, 3, 3]
})

avg_score = domains["Score"].mean()

if avg_score < 2:
    maturity = "Emerging"
elif avg_score < 3:
    maturity = "Developing"
elif avg_score < 4:
    maturity = "Connected"
elif avg_score < 4.5:
    maturity = "Predictive"
else:
    maturity = "Intelligent"

col1, col2, col3 = st.columns(3)
col1.metric("Readiness Score", f"{avg_score:.1f}/5")
col2.metric("Maturity Level", maturity)
col3.metric("Assessment Domains", len(domains))

st.markdown("---")

st.subheader("Transformation Readiness by Domain")

fig = px.bar(
    domains,
    x="Domain",
    y="Score",
    text="Score",
    range_y=[0, 5]
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("MetroHealth TransformX Maturity Model")

maturity_model = pd.DataFrame({
    "Level": [
        "Level 1",
        "Level 2",
        "Level 3",
        "Level 4",
        "Level 5"
    ],
    "Stage": [
        "Digital",
        "Connected",
        "Intelligent",
        "Predictive",
        "Adaptive"
    ],
    "Description": [
        "Healthcare data is captured electronically.",
        "Systems exchange information across facilities.",
        "Analytics provide visibility and decision support.",
        "AI supports forecasting, risk detection, and prioritization.",
        "The organization continuously learns and improves."
    ]
})

st.dataframe(maturity_model, use_container_width=True)

st.markdown("---")

st.info(
    f"""
    **Executive Interpretation**

    Current organizational maturity is assessed as **{maturity}**.

    The strongest areas are interoperability, healthcare intelligence,
    and operations intelligence.

    Priority improvement areas include responsible AI governance,
    clinical AI validation, workforce readiness, and data governance.
    """
)

st.success("Transformation Maturity module operational.")