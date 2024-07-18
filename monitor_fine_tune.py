import openai
import json

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def check_fine_tune_status(fine_tune_id):
    response = openai.FineTune.retrieve(fine_tune_id)
    return response

if __name__ == "__main__":
    fine_tune_id = "ft-xxxxxxxxxxxxxxx"  # Replace with your fine-tuning job ID
    response = check_fine_tune_status(fine_tune_id)
    print("Fine-tuning status:", json.dumps(response, indent=2))
