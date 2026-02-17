# 🧾 Multi-Language Invoice Extractor (Vision + LLM)

An AI-powered Invoice Understanding System that extracts structured data from invoice images using Vision-enabled Large Language Models.

This project demonstrates how modern LLMs can replace traditional OCR pipelines by combining image understanding, prompt engineering, and reasoning capabilities.

It transforms unstructured invoice images into structured, queryable information.

---

## 🚀 Key Capabilities

- 🖼️ Upload invoice images (JPG / PNG)
- 🌍 Multi-language invoice support
- 🧠 Vision + LLM-based semantic understanding
- 📊 Extract structured fields (vendor, total, date, items, tax, etc.)
- ❓ Ask custom natural language questions about the invoice
- 💬 Context-aware intelligent responses
- 🎨 Clean Streamlit UI

---

## 🏗️ System Architecture

1. User uploads an invoice image  
2. Image is processed and sent to Gemini Vision model  
3. Model extracts semantic meaning from visual + textual content  
4. Structured data is generated  
5. User can ask follow-up questions about the invoice  
6. Context-aware answers are returned  

This demonstrates real-world AI document understanding.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (Vision + Text)
- Pillow (Image Processing)
- python-dotenv

---

## 📂 Project Structure

invoice-llm-extractor/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .env.example

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/RajhansJain/invoice-llm-extractor.git  
cd invoice-llm-extractor

### 2️⃣ Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Configure API Key

Create a `.env` file in the project root:

GEMINI_API_KEY=your_api_key_here

---

## ▶️ Run Application

streamlit run app.py

---

## 🔐 Security

- No API keys are hardcoded
- Environment variable based configuration
- .env file excluded via .gitignore

---

## 📈 Future Improvements

- Structured JSON export
- Invoice validation checks
- Multi-file batch processing
- OCR fallback integration
- Cloud deployment (Streamlit Cloud / GCP / AWS)

---

## 💡 Why This Project Stands Out

Invoice processing is a real-world business automation problem.

This system demonstrates:

- Vision + Language model integration
- Prompt engineering for structured extraction
- AI-powered document understanding
- End-to-end LLM application development
- Production-style project structuring

---

## 👤 Author

Rajhans Jain  
B.Tech | AI/ML & Data Engineering Enthusiast

