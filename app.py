import streamlit as st
import requests

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Job Fit Analyzer", layout="centered")
st.title("📄💼 Resume vs Job Description Analyzer")

job_desc = st.text_area("📝 Paste Job Description", height=200)
resume = st.text_area("📋 Paste Resume Text", height=200)

if st.button("🔍 Analyze"):
    if not job_desc or not resume:
        st.warning("Please provide both job description and resume.")
    else:
        with st.spinner("Calling the model..."):
            try:
                response = requests.post(API_URL, json={
                    "job_description": job_desc,
                    "resume_text": resume
                })

                if response.status_code == 200:
                    st.markdown(response.text)

                else:
                    st.error(f"API error: {response.status_code}\n{response.text}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
