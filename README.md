# PDF to .docx and .png Conversion Tools

This repository now includes a set of tools designed to facilitate the conversion of PDF documents into .docx format and the extraction of images from PDFs to save them as .png files. This allows for a detailed analysis of concepts with the added benefit of creating visual representations through Excel graphs and organizing images in corresponding folders.

## Update 16th May

We have addressed the previously unsuccessful merge issue for .png extraction and are excited to announce the creation of a new project for extracting data from .docx files. The merge issue was resolved by refining our image extraction process, ensuring that images are now correctly extracted as .png files without any merge conflicts. The new project, focused on .docx data extraction, aims to streamline the process of extracting textual data from .docx files, making it easier to analyze and manipulate document content. This project includes a set of tools and scripts designed to efficiently extract data and save it in a structured format.

## pdf-to-docx Directory

Within the `pdf-to-docx` directory, you will find several key components that make up the conversion toolkit:

- `README.md`: Provides a comprehensive guide on how to use the conversion tools, compile the .docx documents, interpret the Excel graphs, and extract images from PDFs to save them as .png files.
- `convert_pdf_to_docx.py`: A Python script that lists all PDF files in the current directory, allows the user to select a file for conversion, converts its content into .docx format while preserving the initial format and tables, and extracts images to save them as .png files in corresponding folders. This script utilizes libraries such as pdf2docx and PyMuPDF to process PDF content efficiently.
- `analysis.docx`: A .docx file that contains a detailed explanation of all concepts derived from the PDF. This document is structured with sections for each concept and includes comments for clarity and future reference.
- `graph.xlsx`: An Excel file that features a graph visually representing key data and concepts from the analysis. The graph is designed with clear labels on axes and data points for easy interpretation.

## Compiling .docx Documents

To compile the `analysis.docx` file into a .docx document, you can use any software that supports .docx formats. If using the command line, navigate to the `pdf-to-docx` directory and run the following command:

```
pdflatex analysis.tex
```

This will generate a .docx document that includes all the detailed explanations of the concepts derived from the original PDF.

## Interpreting the Excel Graph

The `graph.xlsx` file contains an Excel graph that visually represents the key data and concepts from the analysis. To view and interpret this graph, simply open the file with any software that supports Excel formats. Pay close attention to the labeled axes and data points to fully understand the data presented.

## Using the `convert_pdf_to_docx.py` Script

As part of the conversion process, the script now creates a folder named "transformed file" in the current directory. Inside this folder, a new folder with the name of the converted file (minus the .docx extension) is created. The converted .docx file and extracted .png images are then saved inside their corresponding named folder within "transformed file". This organization helps in managing the converted files and images more efficiently.

## Processing .docx Files with the Gemini API

To further enhance the capabilities of this toolkit, we have integrated the Gemini API for processing .docx files. This addition allows users to automatically analyze and process .docx files in a specified directory, leveraging the Gemini API's powerful analysis capabilities to generate new .docx files with the processed content.

### Setting Up and Using the Gemini API

1. Obtain an API key from Gemini by signing up on their platform.
2. Store your API key and other configuration details in the `docx-to-docx/gemini_api_config.json` file.
3. Use the `docx-to-docx/GeminiAPI_docx_processor.py` script to process .docx files. Simply run the script and follow the prompts to specify the directory containing your .docx files.

This process will read each .docx file in the specified directory, send the content to the Gemini API for analysis, and save the processed content back into new .docx files within the same directory, enabling a seamless workflow for document analysis and processing.

By utilizing these tools, users can efficiently convert PDF documents into detailed .docx analyses, extract images as .png files, visually represent data through Excel graphs, and leverage the Gemini API for advanced document processing, enhancing the understanding and presentation of complex concepts.
