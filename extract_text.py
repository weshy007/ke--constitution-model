import fitz # PyMuPDF
import json

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    return text


def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(text)


if __name__ == "__main__":
    pdf_path = "kenyan_constitution.pdf"
    text = extract_text(pdf_path)
    save_text_to_file(text, "kenyan_constitution.txt")