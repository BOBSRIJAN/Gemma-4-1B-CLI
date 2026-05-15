import torch
import time


def generate_response(model, tokenizer, prompt: str, max_new_tokens: int = 100) -> dict:
    start = time.time()

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    if tokenizer.pad_token is None and tokenizer.eos_token is not None:
        tokenizer.pad_token = tokenizer.eos_token

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    end = time.time()

    return {
        "response": response,
        "generation_time": round(end - start, 2)
    }