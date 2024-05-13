# PDF to .docx and .png Conversion Process

This README explains the process of converting PDF content to .docx format and extracting images to save them as .png files, detailing the use of the `convert_pdf_to_docx.py` script.

## Using the `convert_pdf_to_docx.py` Script

To convert a PDF file to .docx format and extract images as .png files, use the `convert_pdf_to_docx.py` script located in the `pdf-to-docx` directory. The script lists all PDF files in the current directory, allows the user to select a file for conversion, outputs the content in .docx format while preserving the initial format and tables, and extracts images to save them as .png files. For usage, run the following command in your terminal:

```
python convert_pdf_to_docx.py
```

This command will list all PDF files in the current directory. Follow the prompts to select a file, convert it to .docx format, and extract images as .png files.

### New Folder Creation and File Placement Process

As part of the conversion process, the script now creates a folder named "transformed file" in the current directory. Inside this folder, a new folder with the name of the converted file (minus the .docx extension) is created. The converted .docx file and extracted .png images are then saved inside their corresponding named folder within "transformed file". This organization helps in managing the converted files and images more efficiently.
