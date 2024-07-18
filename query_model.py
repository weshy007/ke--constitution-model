import openai
from decouple import config

# Set your OpenAI API key
openai.api_key = config('OPENAI_API_KEY')

def query_model(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "What does Article 1 of the Kenyan Constitution state?"
    response = query_model(prompt)
    print("Response:", response)
