import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MetroHealth Transformation Index",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MetroHealth TransformX Index™")
st.subheader("Healthcare Interoperability, Intelligence & AI Transformation Score")

st.markdown(
    """
    The MetroHealth TransformX Index™ measures how ready a healthcare organization is
    to operate as a connected, intelligent, AI-enabled, and continuously learning health ecosystem.
    """
)

st.markdown("---")

index = pd.DataFrame({
    "Pillar": [
        "Interoperability",
        "Healthcare Intelligence",
        "Clinical AI",
        "Operations Intelligence",
        "Responsible AI Governance",
        "Digital Transformation",
        "Workforce Readiness"
    ],
    "Score": [84, 81, 76, 86, 72, 79, 70]
})

overall_index = round(index["Score"].mean(), 1)

if overall_index >= 85:
    category = "Transformation Leader"
elif overall_index >= 75:
    category = "Transformation Ready"
elif overall_index >= 60:
    category = "Developing Intelligence"
elif overall_index >= 45:
    category = "Connected Foundation"
else:
    category = "Emerging"

col1, col2, col3 = st.columns(3)
col1.metric("MetroHealth Index Score", f"{overall_index}/100")
col2.metric("Transformation Category", category)
col3.metric("Pillars Assessed", len(index))

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Index Score by Pillar")
    fig = px.bar(
        index,
        x="Pillar",
        y="Score",
        text="Score",
        range_y=[0, 100]
    )
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Transformation Index Distribution")
    fig = px.line_polar(
        index,
        r="Score",
        theta="Pillar",
        line_close=True
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Index Interpretation")

st.info(
    f"""
    MetroHealth TransformX Index Score: **{overall_index}/100**

    Current Category: **{category}**

    Interpretation:

    The organization demonstrates strong progress toward connected,
    intelligent, AI-enabled healthcare. Interoperability, healthcare intelligence,
    and operations intelligence are maturing well.

    Priority improvement areas include responsible AI governance,
    workforce readiness, and clinical AI validation.
    """
)

st.markdown("---")

st.subheader("Index Categories")

categories = pd.DataFrame({
    "Score Range": [
        "0–44",
        "45–59",
        "60–74",
        "75–84",
        "85–100"
    ],
    "Category": [
        "Emerging",
        "Connected Foundation",
        "Developing Intelligence",
        "Transformation Ready",
        "Transformation Leader"
    ],
    "Meaning": [
        "Early digital maturity with limited integration.",
        "Basic connectivity and foundational digital systems.",
        "Analytics and intelligence capabilities are developing.",
        "Strong readiness for AI-enabled transformation.",
        "Advanced learning healthcare ecosystem."
    ]
})

st.dataframe(categories, use_container_width=True)

st.success("MetroHealth TransformX Index™ operational.")