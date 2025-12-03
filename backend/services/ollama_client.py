# services/ollama_client.py
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
CHAT_MODEL = os.getenv("CHAT_MODEL", "llama3.1")


def ollama_chat(system_msg: str, user_msg: str) -> str:
    """
    Handles Ollama chat with streaming chunks.
    Combines all partial responses into one final string.
    """

    payload = {
        "model": CHAT_MODEL,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "stream": True
    }

    response = requests.post(
        f"{OLLAMA_URL}/api/chat", json=payload, stream=True
    )

    full_reply = ""

    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode("utf-8"))
            if "message" in data and "content" in data["message"]:
                full_reply += data["message"]["content"]
        except json.JSONDecodeError:
            continue

    return full_reply.strip()
