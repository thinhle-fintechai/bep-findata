# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import time
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from src.prompts.ocr_prompt import get_input_prompt
from src.utils.files import read_file, write_file, load_pdf_data
from src.utils.formater import clean_json_content

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

load_dotenv()

def generate():
    # Start timing
    start_time = time.time()
    print(f"Bắt đầu xử lý PDF lúc: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
    
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"

    # Time: Loading files
    load_start = time.time()
    json_format = read_file("./financial_metrics/metrics.json")
    
    # Load PDF data (base64 encoded)
    pdf_data = load_pdf_data("./docs/poor_2.pdf")
    load_time = time.time() - load_start
    print(f"Thời gian load files: {load_time:.2f} giây")
    
    # Time: Preparing content
    prep_start = time.time()
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=get_input_prompt(json_format)),
                types.Part.from_bytes(
                    data=base64.b64decode(pdf_data),
                    mime_type="application/pdf"
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )
    prep_time = time.time() - prep_start
    print(f"Thời gian chuẩn bị: {prep_time:.2f} giây")

    # Time: AI Processing
    ai_start = time.time()
    print("Bắt đầu xử lý với Gemini AI...")

    # Collect all chunks before writing to file
    full_response = ""
    chunk_count = 0
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # Handle None values in streaming chunks
        if chunk.text is not None:
            print(chunk.text, end="")
            full_response += chunk.text
            chunk_count += 1
        else:
            print("\nGặp chunk không có text, dừng stream")
            break
    
    ai_time = time.time() - ai_start
    print(f"\nThời gian AI xử lý: {ai_time:.2f} giây ({chunk_count} chunks)")
    
    # Time: Post-processing
    post_start = time.time()
    print("Đang làm sạch và lưu JSON...")
    
    # Clean and format JSON before writing to file
    cleaned_json = clean_json_content(full_response)
    output_filename = f"./output/output_{int(time.time())}.json"
    write_file(output_filename, cleaned_json)
    
    post_time = time.time() - post_start
    total_time = time.time() - start_time
    
    # Summary
    print(f"\n📊 TỔNG KẾT THỜI GIAN:")
    print(f"├── Load files: {load_time:.2f}s")
    print(f"├── Chuẩn bị: {prep_time:.2f}s") 
    print(f"├── AI xử lý: {ai_time:.2f}s ({ai_time/total_time*100:.1f}%)")
    print(f"├── Hậu xử lý: {post_time:.2f}s")
    print(f"└── TỔNG CỘNG: {total_time:.2f}s")
    print(f"\n✅ Hoàn thành! File lưu tại: {output_filename}")
    
    return total_time


if __name__ == "__main__":
    try:
        total_time = generate()
        print(f"\n🎯 Kết thúc xử lý thành công trong {total_time:.2f} giây")
    except Exception as e:
        print(f"\n❌ Lỗi xảy ra: {e}")
        raise