import PyPDF2
import re

def convert_pdf_to_latex(pdf_path, latex_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        # Initialize a string to hold the LaTeX content
        latex_content = ""

        # Loop through each page in the PDF
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Convert the extracted text to LaTeX syntax
            # This is a simplified example and might need adjustments for complex PDFs
            text = text.replace('&', '\\&')
            text = text.replace('%', '\\%')
            text = re.sub(r'([#$_{}])', r'\\\1', text)

            # Add the text to the LaTeX content, wrapped in a paragraph
            latex_content += f"\\paragraph{{Page {page_num + 1}}}\n{text}\n"

        # Write the LaTeX content to the specified file
        with open(latex_path, 'w') as latex_file:
            latex_file.write(latex_content)

if __name__ == "__main__":
    # Example usage
    convert_pdf_to_latex('example.pdf', 'output.tex')
