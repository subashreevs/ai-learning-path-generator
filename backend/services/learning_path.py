# services/learning_path.py
from .ollama_client import ollama_chat

def extract_skills_from_resume(text: str):
    system_msg = "You are an AI that extracts technical skills from resume text."
    user_msg = f"Extract important skills from this resume:\n\n{text}"
    return ollama_chat(system_msg, user_msg)

def generate_learning_path(raw_text: str, target_role: str):
    system_msg = "You are an AI that builds a detailed step-by-step learning roadmap."
    user_msg = f"""
    Given the following information, create a detailed learning path
    broken into phases with goals, topics, resources, and projects.

    TEXT:
    {raw_text}

    TARGET ROLE:
    {target_role}
    """
    return ollama_chat(system_msg, user_msg)