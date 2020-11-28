from typing import Optional
from xhtml2pdf import pisa
from fastapi.responses import FileResponse
import tempfile
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"

class HTML(BaseModel):
    body_html: Optional[str] = 'Hello World'
    header_html: Optional[str] = ""

@app.post('/pdf')
def renderPDF(html: HTML):
    source_html = """
    <!DOCTYPE html>
    <html>
    """

    source_html += """
    <head>
    """

    source_html += html.header_html

    source_html += """
    </head>
        <body>
    """
    source_html += html.body_html
    source_html += """
        </body>
    </html>
    """

    print(source_html)

    with tempfile.NamedTemporaryFile("w+b", delete = False, suffix=".pdf") as result_file:
        output_filename = result_file.name

        # print(output_filename)

        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
                source_html,                # the HTML to convert
                dest=result_file)           # file handle to recieve result

        # close output file
        # result_file.close()                 # close output file

        return FileResponse(output_filename)