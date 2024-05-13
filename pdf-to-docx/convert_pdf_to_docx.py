import os
from pdf2docx import Converter

def list_pdf_files():
    """List all PDF files in the current directory."""
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    return pdf_files

def select_pdf_file(pdf_files):
    """Allow user to select a PDF file from the list."""
    print("Available PDF files:")
    for i, file in enumerate(pdf_files):
        print(f"{i + 1}. {file}")
    choice = int(input("Enter the number of the PDF file you want to convert: ")) - 1
    return pdf_files[choice]

def convert_pdf_to_docx(pdf_file):
    """Convert the selected PDF to a .docx file while preserving the initial format and tables."""
    docx_file = pdf_file.replace('.pdf', '.docx')
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"Converted '{pdf_file}' to '{docx_file}' successfully.")

def main():
    pdf_files = list_pdf_files()
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    selected_pdf = select_pdf_file(pdf_files)
    convert_pdf_to_docx(selected_pdf)

if __name__ == "__main__":
    main()
