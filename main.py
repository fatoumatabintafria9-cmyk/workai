from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jobs = []

class Job(BaseModel):
    title: str
    company: str
    location: str
    salary: str
    experience: str


@app.get("/")
def home():
    return {"message": "WorkAI Backend connecté 🚀"}


@app.post("/create-job")
def create_job(job: Job):
    jobs.append(job.dict())
    return {"message": "Offre créée"}


@app.get("/jobs")
def get_jobs():
    return jobs