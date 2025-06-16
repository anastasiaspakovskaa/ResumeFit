from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from analyze_fit import analyze_resume_fit

app = FastAPI()

class AnalysisRequest(BaseModel):
    job_description: str
    resume_text: str

@app.post("/analyze")
def analyze(data: AnalysisRequest):
    try:
        result = analyze_resume_fit(data.job_description, data.resume_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
