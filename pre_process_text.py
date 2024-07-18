import json

def preprocess_text(text):
    # Split text into chunks (you can customize this based on the structure of the constitution)
    chunks = text.split("\n\n")  # Assuming paragraphs are separated by double newlines
    data = []
    for chunk in chunks:
        prompt = "What does this section of the Kenyan Constitution say?"
        completion = chunk.strip()
        data.append({"prompt": prompt, "completion": completion})
    return data

def save_to_jsonl(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for entry in data:
            json.dump(entry, file)
            file.write('\n')

if __name__ == "__main__":
    with open("kenyan_constitution.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    data = preprocess_text(text)
    save_to_jsonl(data, "constitution.jsonl")
