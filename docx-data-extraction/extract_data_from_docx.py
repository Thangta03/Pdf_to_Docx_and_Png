import docx
import json
import os
from typing import List, Dict

def extract_text_from_docx(docx_path: str) -> List[str]:
    """
    Extracts text from a DOCX file and returns it as a list of paragraphs.
    """
    try:
        doc = docx.Document(docx_path)
        return [paragraph.text for paragraph in doc.paragraphs]
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return []

def save_data_to_json(data: List[Dict[str, str]], output_path: str) -> None:
    """
    Saves extracted data to a JSON file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving data to {output_path}: {e}")

def extract_data_from_docx(docx_path: str, output_path: str) -> None:
    """
    Extracts data from a DOCX file and saves it in a structured JSON format.
    """
    text = extract_text_from_docx(docx_path)
    data = [{"paragraph": i, "text": paragraph} for i, paragraph in enumerate(text, start=1)]
    save_data_to_json(data, output_path)

if __name__ == "__main__":
    docx_file = input("Enter the path to the DOCX file: ")
    output_file = input("Enter the path for the output JSON file: ")
    if not os.path.exists(docx_file):
        print(f"The file {docx_file} does not exist.")
    else:
        extract_data_from_docx(docx_file, output_file)
        print(f"Data extracted and saved to {output_file}.")
