import json
import openai

from decouple import config

# Set your OpenAI API key
openai.api_key = config('OPENAI_API_KEY')

# def fine_tune_model(training_file):
#     response = openai.FineTune.create(
#         training_file=training_file,
#         model="gpt-3.5-turbo"
#     )
#     return response

# if __name__ == "__main__":
#     training_file = "constitution.jsonl"  # Path to your JSONL file
#     response = fine_tune_model(training_file)
#     print("Fine-tuning response:", response)


def upload_file(file_path):
    response = openai.File.create(
        file=open(file_path, "rb"),
        purpose='fine-tune'
    )
    return response

def create_fine_tune_job(training_file_id):
    response = openai.FineTuningJob.create(
        model="gpt-3.5-turbo",
        training_file=training_file_id
    )
    return response

if __name__ == "__main__":
    training_file_path = "constitution.jsonl"  # Path to your JSONL file
    upload_response = upload_file(training_file_path)
    training_file_id = upload_response['id']
    
    print("Uploaded file ID:", training_file_id)
    
    fine_tune_response = create_fine_tune_job(training_file_id)
    print("Fine-tuning response:", json.dumps(fine_tune_response, indent=2))