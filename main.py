
import traceback
from core.initialize import initialize_model
from services.generator import generate_response


def main():

    try:
        tokenizer, model = initialize_model()
        print("Model initialized successfully!")

        while True:
            prompt = input("\nYou: ")
            
            if prompt.lower() in ["exit", "quit"]:
                break

            result = generate_response(
                model=model,
                tokenizer=tokenizer,
                prompt=prompt,
                max_new_tokens=100,
            )

            print(f"\nAI ({result['generation_time']} sec):")
            print(result["response"])

    except KeyboardInterrupt:
        print("\nApplication stopped.")

    except Exception as e:
        print("\nUnexpected error:")
        print(type(e).__name__, str(e))
        traceback.print_exc()

if __name__ == "__main__":
    main()