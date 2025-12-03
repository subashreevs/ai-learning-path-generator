# models/learning_path_models.py
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class TopicRequest(BaseModel):
    topic: str

class ResumeResponse(BaseModel):
    extracted_text: str

class RoadmapResponse(BaseModel):
    roadmap: str