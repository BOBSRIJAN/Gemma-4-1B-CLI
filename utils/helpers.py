from pathlib import Path

def has_local_model_files(model_dir: Path) -> bool:
    required_files = [
        "config.json",
        "tokenizer.json",
        "tokenizer_config.json",
    ]

    return all((model_dir / file).exists() for file in required_files)