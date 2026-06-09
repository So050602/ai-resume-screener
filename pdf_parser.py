import pdfplumber
import re

def extract_text(pdf_file):

    text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        # Remove weird PDF artifacts
        text = re.sub(r'\(cid:\d+\)', ' ', text)

        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)

    except Exception as e:
        print(e)

    return text