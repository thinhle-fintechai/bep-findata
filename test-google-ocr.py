# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyAyd_hP7T2mTMfsGUhvcLpHWV3g2u-AYS8",
    )

    model = "gemini-2.5-flash"

    json_format = read_file("financial_metrics.json")
    
    # Load PDF data (base64 encoded)
    pdf_data = load_pdf_data()
    
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Từ báo cáo tài chính này hãy trích suất dữ liệu bảng cân bằng kế toán, báo cáo kết quả hoạt động kinh doanh, báo cáo lưu chuyển tiền tệ dưới dạng json như format sau tôi gửi cho bạn, lưu ý những con số phải được trích suất từ báo cáo tài chính này.

Json format:
{json_format}"""),
                types.Part.from_bytes(
                    data=base64.b64decode(pdf_data),
                    mime_type="application/pdf"
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def load_pdf_data():
    """
    Load PDF data and convert it to base64 string.
    """
    try:
        with open("bctc.pdf", "rb") as file:
            pdf_bytes = file.read()
            return base64.b64encode(pdf_bytes).decode('utf-8')
    except FileNotFoundError:
        print("Error: bctc.pdf file not found!")
        print("Please make sure the PDF file exists in the current directory")
        raise

if __name__ == "__main__":
    generate()
