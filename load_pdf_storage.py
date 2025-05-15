# *************** IMPORT LIBRARY ***************
from PyPDF2 import PdfReader

# *************** FUNCTION ***************
def load_pdf_from_local(path):
    """
    Load text content from a local PDF file.

    Args:
        path (str): The file path of the local PDF.

    Returns:
        str: Extracted text from all pages joined by newlines.
    """
    try:
        reader = PdfReader(path)
        return "\n".join([page.extract_text() for page in reader.pages])
    except Exception as error:
        print(f"An error occurred (load_pdf_from_local): {error}")
        return ""

# *************** MAIN ***************
if __name__ == "__main__":
    try:
        text = load_pdf_from_local("example.pdf")
        print("Local PDF:\n", text[:300])
    except Exception as main_error:
        print("Local PDF error:", main_error)

