from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# 📝 Sample inputs
job_description = """
We are looking for a Python developer with experience in building REST APIs, working with FastAPI or Flask, and deploying apps to AWS. Bonus points for experience with CI/CD and Docker.
"""

resume_text = """
Experienced backend developer with 3 years of Python experience. Built several internal tools using Flask and Django. Recently learning AWS, deployed a personal project using EC2 and S3. Familiar with Docker basics.
"""
def analyze_resume_fit(job_description: str, resume_text: str):
    prompt = f"""
        You are a career coach.
        
        Compare the resume to the job description and return:
        - fit_score: a number between 0 and 100
        - summary: short paragraph
        - strengths: list of 3 bullet points
        - weaknesses: list of 3 bullet points
        - suggestions: list of 3 improvement suggestions
        
        Job Description:
        \"\"\"{job_description}\"\"\"
        
        Resume:
        \"\"\"{resume_text}\"\"\"
        """

    client = Groq(
        api_key=os.getenv("GROQ_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content
