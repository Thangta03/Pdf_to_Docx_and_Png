import os
import subprocess
import sys

def install_missing_packages():
    """Check and install missing packages."""
    try:
        from pdf2image import convert_from_path  # instead of fitz
        import pdf2docx
    except ImportError as e:
        missing_package = str(e).split(" ")[-1]
        print(f"Installing missing package: {missing_package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", missing_package])

def list_pdf_files():
    """List all PDF files in the current directory."""
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    return pdf_files

def select_pdf_file(pdf_files):
    """Allow user to select a PDF file from the list."""
    print("Available PDF files:")
    for i, file in enumerate(pdf_files):
        print(f"{i + 1}. {file}")
    while True:
        try:
            choice = int(input("Enter the number of the PDF file you want to convert: ")) - 1
            if 0 <= choice < len(pdf_files):
                return pdf_files[choice]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

from pdf2image import convert_from_path
import pdf2docx

def extract_images_from_pdf(pdf_file):
    """Extract images from the PDF and save them as .png files."""
    try:
        images = convert_from_path(pdf_file)
        image_dir = os.path.splitext(pdf_file)[0] + "_images"
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
    except Exception as e:
        print(f"An error occurred while creating the directory '{image_dir}': {e}")
        return

    for i, image in enumerate(images):
        image_filename = f"{image_dir}/image_page_{i + 1}.png"
        image.save(image_filename, 'PNG')
    print(f"Extracted images from '{pdf_file}' to '{image_dir}' successfully.")
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = f"{image_dir}/image_page_{i + 1}_xref_{xref}.png"
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
    print(f"Extracted images from '{pdf_file}' to '{image_dir}' successfully.")
    
def convert_pdf_to_docx(pdf_file):
    """Convert the selected PDF to a .docx file while preserving the initial format and tables."""
    try:
        import pdf2docx
        from pdf2docx import Converter
        # Create "transformed file" directory if it does not exist
        transformed_dir = "transformed file"
        if not os.path.exists(transformed_dir):
            os.makedirs(transformed_dir)
    except Exception as e:
        print(f"An error occurred while creating the directory '{transformed_dir}': {e}")
        return

    try:
        # Create a new folder named after the converted file (without the .docx extension) inside the "transformed file" directory
        file_name_without_extension = os.path.splitext(pdf_file)[0]
        final_dir = os.path.join(transformed_dir, file_name_without_extension)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
    except Exception as e:
        print(f"An error occurred while creating the directory '{final_dir}': {e}")
        return

    # Update the file path for saving the converted .docx file to be within the newly created folder
    docx_file = os.path.join(final_dir, file_name_without_extension + '.docx')
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f"Converted '{pdf_file}' to '{docx_file}' successfully.")
    
    # Extract and save images from the PDF
    extract_images_from_pdf(pdf_file)

def main():
    install_missing_packages()
    pdf_files = list_pdf_files()
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    selected_pdf = select_pdf_file(pdf_files)
    convert_pdf_to_docx(selected_pdf)

if __name__ == "__main__":
    main()
