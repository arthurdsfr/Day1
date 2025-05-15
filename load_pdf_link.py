# *************** IMPORT LIBRARY ***************
import requests
from PyPDF2 import PdfReader

# *************** IMPORT HELPER ***************
import load_pdf_storage as storage

# *************** FUNCTION ***************
def load_pdf_from_url(url):
    """
    Download a PDF from the given URL and extract its content.

    Args:
        url (str): The URL of the PDF file.

    Returns:
        str: Extracted text content from the downloaded PDF.
    """
    try:
        response = requests.get(url)
        with open("temp.pdf", "wb") as temp_file:
            temp_file.write(response.content)

        content = storage.load_pdf_from_local("temp.pdf")
        return content

    except Exception as error:
        print(f"An error occurred (load_pdf_from_url): {error}")
        return ""

# *************** MAIN ***************
if __name__ == "__main__":
    try:
        url = "https://arxiv.org/pdf/2106.14834.pdf"
        text = load_pdf_from_url(url)
        print("URL PDF:\n", text[:300])
    except Exception as main_error:
        print("URL PDF error:", main_error)
