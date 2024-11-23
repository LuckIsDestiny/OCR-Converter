from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
import subprocess

app = FastAPI()

# Serve the HTML file for the user interface
@app.get("/", response_class=FileResponse)
def index():
    return "index.htm"

# Serve static files from the "static" directory
@app.get("/static/{fn}", response_class=FileResponse)
async def static(fn: str):
    return f"static/{fn}"

# Process the uploaded file for OCR and return the resulting PDF file
@app.post("/ocr", response_class=FileResponse)
async def ocr(
    optimize: int = Form(...),
    forceOCR: bool = Form(False),
    language: str = "eng",
    file: UploadFile = File(...)
):
    # Ensure only one file is uploaded
    if not file:
        raise Exception("Need exactly one file!")

    # Create a temporary output file
    f_out = NamedTemporaryFile(suffix=".pdf", delete=False)

    # Write the uploaded file to a temporary input file
    with NamedTemporaryFile(suffix=".pdf", mode="wb") as f_in:
        content = await file.read()
        f_in.write(content)
        f_in.flush()

        # Determine the OCR mode
        ocr_flag = "--force-ocr" if forceOCR else "--redo-ocr"

        # Run OCR command
        proc = subprocess.Popen(
            ["ocrmypdf", ocr_flag, "--clean", f"--optimize={optimize}", "-l", language, f_in.name, f_out.name]
        )

        # Wait for OCR to finish
        code = proc.wait()

        # Set the OCR exit code in the response header
        response = FileResponse(f_out.name)
        response.headers["X-OCR-Exit-Code"] = str(code)

        return response
