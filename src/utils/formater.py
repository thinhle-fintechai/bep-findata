import re
import json


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