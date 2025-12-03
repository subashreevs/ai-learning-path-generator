from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.pdf_parser import extract_text_from_pdf
from services.learning_path import generate_learning_path

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
#  Pydantic Models
# -------------------------

class TopicRequest(BaseModel):
    topic: str

class TextRequest(BaseModel):
    text: str

# -------------------------
#  Endpoints
# -------------------------

@app.post("/generate")
async def generate_from_topic(body: TopicRequest):
    roadmap = generate_learning_path(body.topic, "general")
    return {"roadmap": roadmap}

@app.post("/generate-from-text")
async def generate_from_text(body: TextRequest):
    roadmap = generate_learning_path(body.text, "general")
    return {"roadmap": roadmap}

@app.post("/generate-from-pdf")
async def generate_from_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    roadmap = generate_learning_path(text, "general")
    return {"roadmap": roadmap}

@app.get("/")
async def root():
    return {"message": "AI Learning Path Generator Running!"}