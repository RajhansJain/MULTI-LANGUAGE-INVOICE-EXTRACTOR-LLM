# 🧾 Multi-Language Invoice Extractor (Vision + LLM)

An AI-powered Invoice Understanding System that extracts structured information from invoice images using Large Language Models.

This application allows users to upload invoice images (any language), ask custom questions, and receive intelligent, context-aware responses.

---

## 🚀 Features

- Upload invoice image (JPG / PNG)
- Multi-language invoice support
- Extract structured fields (vendor, total, date, items, etc.)
- Ask custom natural language questions about the invoice
- Context-aware LLM responses
- Clean Streamlit interface

---

## 🏗️ How It Works

1. User uploads an invoice image
2. Image is processed and passed to LLM
3. LLM analyzes visual + textual content
4. User asks questions like:
   - What is the total amount?
   - Who is the vendor?
   - What is the invoice date?
5. System generates intelligent answers

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (Vision + Text)
- PIL (Image Processing)
- dotenv

---

## 📂 Project Structure

```
invoice-llm-extractor/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .env.example
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RajhansJain/invoice-llm-extractor.git
cd invoice-llm-extractor
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

Create a `.env` file in project root:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🔐 Security

- No API keys are hardcoded
- Uses environment variables for secure key handling

---

## 📈 Future Improvements

- Automatic structured JSON extraction
- Invoice validation checks
- Multi-file batch processing
- OCR fallback integration
- Cloud deployment

---

## 💡 Why This Project Matters

Invoice processing is a common real-world business task.

This system demonstrates:

- Vision + Language model integration
- Prompt engineering for structured extraction
- AI-powered document understanding
- End-to-end LLM application development

---

## 👤 Author

**Rajhans Jain**  
B.Tech | AI/ML & Data Engineering Enthusiast
