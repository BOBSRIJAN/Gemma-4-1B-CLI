import torch

from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM


def download_model(model_id: str, token: str, cache_dir: str, save_dir: str) -> tuple:
    login(token=token)
    print("Downloading tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        token=token,
        cache_dir=cache_dir,
    )

    print("Downloading model...")

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        token=token,
        cache_dir=cache_dir,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )

    print("Saving model locally...")

    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)

    return tokenizer, model
