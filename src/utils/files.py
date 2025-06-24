import base64


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)

def load_pdf_data(file_path):
    """
    Load PDF data and convert it to base64 string.
    """
    try:
        with open(file_path, "rb") as file:
            pdf_bytes = file.read()
            return base64.b64encode(pdf_bytes).decode('utf-8')
    except FileNotFoundError:
        print("Please make sure the PDF file exists in the current directory")
        raise