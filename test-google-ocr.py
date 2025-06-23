# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import time
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate():
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"

    json_format = read_file("financial_metrics.json")
    
    # Load PDF data (base64 encoded)
    pdf_data = load_pdf_data()
    
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Bạn là một chuyên viên phân tích tài chính. Hãy đọc file PDF báo cáo tài chính này. Trích xuất dữ liệu từ các Bảng Cân đối kế toán, Báo cáo Kết quả kinh doanh, và Báo cáo Lưu chuyển tiền tệ. Định dạng đầu ra phải là một file JSON tuân thủ nghiêm ngặt theo cấu trúc sau: {json_format}. Chú ý: các số trong ngoặc đơn () phải được chuyển thành số âm. Nếu một mục không có dữ liệu, hãy để giá trị là null."""),
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

    # Collect all chunks before writing to file
    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        full_response += chunk.text
    
    # Clean and format JSON before writing to file
    cleaned_json = clean_json_content(full_response)
    write_file(f"./output/output_{time.time()}.json", cleaned_json)

def clean_json_content(content):
    """
    Clean JSON content by removing markdown code blocks and formatting properly.
    """
    # Remove markdown code blocks (```json and ```)
    content = re.sub(r'^```json\s*\n?', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n?```\s*$', '', content, flags=re.MULTILINE)
    content = content.strip()
    
    try:
        # Parse and reformat JSON to ensure it's valid and properly formatted
        parsed_json = json.loads(content)
        return json.dumps(parsed_json, indent=2, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"Warning: Could not parse JSON content: {e}")
        print("Saving raw content...")
        return content

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)

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
