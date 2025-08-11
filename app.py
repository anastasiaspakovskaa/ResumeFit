import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Job Fit Analyzer", layout="centered")
st.title("📄💼 Resume vs Job Description Analyzer")

job_desc = st.text_area("📝 Paste Job Description", height=200)
resume = st.text_area("📋 Paste Resume Text", height=200)

response = "{\n  \"fit_score\": 80,\n  \"summary\": \"Strong Python background with relevant experience in building backend applications\",\n  \"strengths\": [\n    \"Experience with Python and Flask\",\n    \"Familiarity with Docker\",\n    \"Recent experience with AWS deployment\"\n  ],\n  \"weaknesses\": [\n    \"Limited experience with REST APIs\",\n    \"No experience with FastAPI\",\n    \"Basic knowledge of Docker\"\n  ],\n  \"suggestions\": [\n    \"Highlight REST API experience from previous projects\",\n    \"Invest in learning FastAPI for improved job prospects\",\n    \"Develop advanced Docker skills for better deployment options\"\n  ]\n}"

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
                    try:
                        first_pass = json.loads(response.text)
                        if isinstance(first_pass, str):
                            data = json.loads(first_pass)
                        else:
                            data = first_pass

                        st.subheader("💯 Fit Score")
                        st.write(f"**{data['fit_score']}**")

                        st.subheader("📝 Summary")
                        st.write(data["summary"])

                        st.subheader("✅ Strengths")
                        for item in data["strengths"]:
                            st.markdown(f"- {item}")

                        st.subheader("⚠️ Weaknesses")
                        for item in data["weaknesses"]:
                            st.markdown(f"- {item}")

                        st.subheader("💡 Suggestions")
                        for item in data["suggestions"]:
                            st.markdown(f"- {item}")

                    except Exception as e:
                        st.error("Response couldn't be parsed as JSON. Here's the raw output:")
                        st.text(response.text)

                else:
                    st.error(f"API error: {response.status_code}\n{response.text}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
