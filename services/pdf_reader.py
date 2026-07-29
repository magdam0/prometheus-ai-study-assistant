import fitz

def extract_text(pdf_bytes):
    """
    Extracts text from a PDF uploaded via Streamlit.
    Returns a single string containing all pages.
    """

    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    pages = []

    for page in pdf:
        pages.append(page.get_text())

    pdf.close()

    return "\n".join(pages)