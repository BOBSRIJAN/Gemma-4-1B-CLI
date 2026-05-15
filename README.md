# Gemma-4-1B-CLI (Custom CLI Version)

A minimal, custom-built **Gemma Inference CLI** using Hugging Face Transformers. This project can:

- **Run fully offline** if the model files already exist locally.
- **Download + cache** the model and tokenizer from Hugging Face when local files are missing.
- Provide a simple interactive prompt loop.

> Model targeted by this CLI: **`google/gemma-3-1b-it`** (configured in `config/settings.py`).

---

## Features

- **Offline-first behavior**
  - If local model files exist under `models/gemma-3-1b-it/`, the app loads with `HF_HUB_OFFLINE=1`.
  - Otherwise, it downloads from Hugging Face using an API token.

- **Simple interactive chat**
  - Type a prompt, get a completion.
  - Type `exit` or `quit` to stop.

- **Deterministic generation**
  - Uses `do_sample=False` and `model.generate(...)`.

---

## Project Structure

- `main.py`
  - Starts the CLI loop and prints generation time.

- `config/settings.py`
  - Defines:
    - `MODEL_ID`
    - `HF_TOKEN` (from environment)
    - `LOCAL_MODEL_DIR` (offline model location)
    - `LOCAL_CACHE_DIR` (Hugging Face cache)

- `core/initialize.py`
  - Decides offline vs download mode.

- `services/downloader.py`
  - Downloads tokenizer + model and saves them locally.

- `services/loader.py`
  - Loads tokenizer + model from local directory.

- `services/generator.py`
  - Runs inference for a given prompt.

---

## Requirements

This project uses the dependencies listed in `requirements.txt`, including:

- `torch`
- `transformers`
- `huggingface_hub`
- `python-dotenv`

> Note: Your environment must be compatible with the installed PyTorch/Transformers versions.

---

## Setup

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Hugging Face token (only needed if local model is missing)

Create a `.env` file in `Gemma-4-1B-CLI/` directory with:

```env
Hugging_Face=YOUR_HF_TOKEN_HERE
```

The code reads `HF_TOKEN = os.getenv("Hugging_Face")`.

---

## How it works (Offline vs Download)

### Offline mode

If these files exist in:

- `models/gemma-3-1b-it/config.json`
- `models/gemma-3-1b-it/tokenizer.json`
- `models/gemma-3-1b-it/tokenizer_config.json`

then:

- The app loads directly from `models/gemma-3-1b-it/`
- It sets `os.environ["HF_HUB_OFFLINE"] = "1"`

### Download mode

If local model files are missing:

- If `Hugging_Face` token is not set, it raises `TokenMissingError`
- It downloads to `hf_cache/`
- It saves the model + tokenizer into `models/gemma-3-1b-it/`

---

## Run the CLI

From the `Gemma-4-1B-CLI/` folder:

```bash
python main.py
```

You’ll see:

- `Model initialized successfully!`
- Then a prompt like:

```text
You: <type here>
```

Stop the app by typing:

- `exit`
- or `quit`

---

## Docker (Optional)

Build the image:

```bash
docker build -t gemma-cli -f Dockerfile .
```

Run:

```bash
docker run --rm gemma-cli
```

### Token in Docker

If the model is not already present locally inside the container, you must provide the token via environment variable `Hugging_Face` (the code uses `python-dotenv` too, but container env is the most reliable):

```bash
docker run --rm -e Hugging_Face=YOUR_HF_TOKEN_HERE gemma-cli
```

---

## Notes / Tuning

- In `main.py`, inference is called with:
  - `max_new_tokens=100`
- In `services/generator.py`:
  - `do_sample=False`
  - generation time is measured and printed

You can modify these defaults in `main.py` / `services/generator.py`.

---