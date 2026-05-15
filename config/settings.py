from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_ID = "google/gemma-3-1b-it"

HF_TOKEN = os.getenv("Hugging_Face")

LOCAL_MODEL_DIR = BASE_DIR / "models" / "gemma-3-1b-it"
LOCAL_CACHE_DIR = BASE_DIR / "hf_cache"

LOCAL_MODEL_DIR.mkdir(parents=True, exist_ok=True)
LOCAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)