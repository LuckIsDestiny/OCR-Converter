# OCR Converter

OCR Converter is a web application built using **FastAPI** and **Dropzone.js** that allows users to upload PDF files and process them using OCR (Optical Character Recognition) to make the text selectable and searchable. The OCR process is powered by **ocrmypdf** in a Dockerized environment.

## Features
- Upload PDF files through drag-and-drop or file selection.
- Choose the OCR optimization level (Low, Medium, High).
- Process PDF files using OCR to make the text selectable and searchable.
- Download the processed PDFs after OCR completion.
- User-friendly UI built with HTML and styled with CSS.

## Tech Stack
- **Backend**: FastAPI (Python)
- **OCR Engine**: ocrmypdf
- **Frontend**: HTML, CSS, Dropzone.js
- **Containerization**: Docker
- **OCR Library**: Python `ocrmypdf` library

## Getting Started

### Prerequisites

- Docker
- Python 3.x
- `ocrmypdf` library for OCR processing

### Setup

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_folder>
    ```

2. **Build the Docker image:**

    First, make sure Docker is installed and running on your machine.

    ```bash
    docker build -t ocr-converter .
    ```

3. **Run the Docker container:**

    Once the image is built, run the container:

    ```bash
    docker run -d -p 8000:8000 ocr-converter
    ```

4. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`. The application interface should appear, where you can upload your PDF files for OCR processing.


## License
OCR Converter is licensed under the GNU GPL v3.
