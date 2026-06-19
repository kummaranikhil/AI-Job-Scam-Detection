import pdfplumber
from docx import Document


def read_pdf(uploaded_file):
    """
    Extract text from a PDF file.
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(uploaded_file):
    """
    Extract text from a DOCX file.
    """

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_text(uploaded_file):
    """
    Automatically detect file type and extract text.
    """

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return read_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return read_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        return None