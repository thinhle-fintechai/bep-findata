## Quick Start Guide

### Step 1: Setup Environment

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd bep-findata
```

2. **Create virtual environment**
```bash
python -m venv .venv
```

3. **Activate virtual environment**
```bash
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Step 2: Configure API Key

1. **Get Gemini API Key**
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Create or login to your account
   - Generate an API key

2. **Create .env file**
```bash
touch .env
```

3. **Add your API key to .env**
```env
GEMINI_API_KEY=your_api_key_here
```

### Step 3: Prepare PDF Files

1. **Add PDF files to docs folder**
```bash
# Make sure your PDF files are in the docs/ directory
ls docs/
# Should show: poor_1.pdf, poor_2.pdf, etc.
```

## How to Run

```bash
python src/ocr/gemini_ocr.py
```

**What happens:**
- Processes `docs/poor_1.pdf` by default
- Shows real-time progress
- Saves result to `output/output_[timestamp].json`
