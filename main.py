from typing import Optional
from xhtml2pdf import pisa
from fastapi.responses import FileResponse
import tempfile
from typing import Optional

from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"

@app.post('/pdf')
def renderPDF(body_html: Optional[str] = Form('Hello World'), header_html: Optional[str] = Form("")):
    source_html = """
    <!DOCTYPE html>
    <html>
    """

    source_html += """
    <head>
    """

    source_html += header_html

    source_html += """
    </head>
        <body>
    """
    source_html += body_html
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