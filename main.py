from typing import Optional
from xhtml2pdf import pisa
from fastapi.responses import FileResponse
import tempfile

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"

@app.get('/pdf')
def renderPDF(text: str):
    source_html = """
        <!DOCTYPE html>
        <html>
            <body>
            """
    source_html += "<h1>" + text + "</h1>"
    source_html += """
            </body>
        </html>
    """

    print(source_html)

    with tempfile.NamedTemporaryFile("w+b", delete = False, suffix=".pdf") as result_file:
        output_filename = result_file.name

        print(output_filename)

        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
                source_html,                # the HTML to convert
                dest=result_file)           # file handle to recieve result

        # close output file
        # result_file.close()                 # close output file

        return FileResponse(output_filename)