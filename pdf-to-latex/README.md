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

## Error Handling Strategies

When using the `convert_pdf_to_docx.py` script, it's important to be aware of potential errors that can occur during the conversion process. This section outlines strategies for handling common errors related to package dependencies and directory creation failures:

- **Package Dependencies**: If you encounter errors related to missing packages, the script attempts to automatically install them. However, if automatic installation fails, please ensure you have the necessary permissions and try installing the packages manually. Detailed error messages are provided to assist in troubleshooting.

- **Directory Creation Failures**: Before creating new directories for the converted files and images, the script checks if the directories already exist to avoid unnecessary errors. If you encounter errors during directory creation, please check the permissions of your current directory and ensure there is enough space available.

Following these strategies can help mitigate common issues encountered during the PDF to .docx and .png conversion process.
