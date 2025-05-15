import requests
from PyPDF2 import PdfReader

def load_pdf_from_local(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages])

def load_pdf_from_url(url):
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)
    content = load_pdf_from_local("temp.pdf")
    return content


if __name__ == "__main__":
    # Local PDF (replace with your own file path)
    try:
        text = load_pdf_from_local("example.pdf")
        print("Local PDF:\n", text[:300])
    except Exception as e:
        print("Local PDF error:", e)

    try:
        url = "https://arxiv.org/pdf/2106.14834.pdf"
        text = load_pdf_from_url(url)
        print("URL PDF:\n", text[:300])
    except Exception as e:
        print("URL PDF error:", e)
