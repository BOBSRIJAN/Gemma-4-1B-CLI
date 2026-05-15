import os

from config.settings import (
    MODEL_ID,
    HF_TOKEN,
    LOCAL_MODEL_DIR,
    LOCAL_CACHE_DIR,
)

from services.downloader import download_model
from services.loader import load_local_model

from utils.helpers import has_local_model_files
from utils.exceptions import (
    TokenMissingError,
)

def initialize_model():
    # Offline mode if model exists
    if has_local_model_files(LOCAL_MODEL_DIR):
        print("Loading local model...")
        os.environ["HF_HUB_OFFLINE"] = "1"

        tokenizer, model = load_local_model(
            str(LOCAL_MODEL_DIR)
        )

    else:
        if not HF_TOKEN:
            raise TokenMissingError(
                "Missing Hugging Face token in .env"
            )

        tokenizer, model = download_model(
            model_id=MODEL_ID,
            token=HF_TOKEN,
            cache_dir=str(LOCAL_CACHE_DIR),
            save_dir=str(LOCAL_MODEL_DIR),
        )

    return tokenizer, model