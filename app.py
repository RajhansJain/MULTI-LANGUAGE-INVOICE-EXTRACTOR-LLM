# streamlit run InvoiceExtractor.py

import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# 1. Load Environment Variables
# --------------------------------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found")
    st.stop()

# --------------------------------------------------
# 2. Create Gemini Client (2026 SDK)
# --------------------------------------------------
client = genai.Client(api_key=API_KEY)

# --------------------------------------------------
# 3. Gemini Vision Response Function
# --------------------------------------------------
def get_gemini_response(system_prompt, image, user_prompt):
    """
    Invoice understanding using Gemini Flash (multimodal)
    """
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=[
            system_prompt,
            image,
            user_prompt
        ]
    )
    return response.text

# --------------------------------------------------
# 4. Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="Gemini Invoice Extractor",
    layout="centered"
)

st.header("📄 Gemini Invoice Extractor Application")

user_input = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader(
    "Choose an image of an Invoice...",
    type=["jpg", "jpeg", "png", "webp"]
)

image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption="Uploaded Invoice Image",
        use_container_width=True
    )

submit = st.button("Tell me about the invoice")

# --------------------------------------------------
# 5. System Prompt
# --------------------------------------------------
system_prompt = """
You are an expert in understanding invoices.
You will receive invoice images and must extract
and explain relevant information such as:
- Invoice number
- Date
- Vendor details
- Line items
- Taxes
- Total amount
"""

# --------------------------------------------------
# 6. Run Model
# --------------------------------------------------
if submit:
    if image is None:
        st.warning("Please upload an invoice image")
    else:
        with st.spinner("Analyzing invoice..."):
            try:
                response = get_gemini_response(
                    system_prompt,
                    image,
                    user_input
                )
                st.subheader("🧠 Extracted Information")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")

# --------------------------------------------------
# ---------------------------------------------------
# Previous version of the code for reference
# before 2024
# ---------------------------------------------------
# import os
# import pathlib
# import textwrap
# from PIL import Image
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemeni_response(input, image, prompt):
#     model = genai.GenerativeModel("models/gemini-flash-latest")
#     response = model.generate_content([input, image[0], prompt])
#     return response.text

# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    

# st.set_page_config(page_title="Gemini Imvoice Extractor", layout="centered")
# st.header("Gemini Invoice Extractor Application")
# input = st.text_input("Input Prompt: ", key="input")
# uploaded_file = st.file_uploader("Choose an image of an Invoice...", type=["jpg", "jpeg", "png"])
# image = ''
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Invoice Image.", use_column_width=True)

# submit=st.button("Tell me about the invoice.")

# input_prompt = """
#                You are an expert in understanding invoices.
#                You will receive input images as invoices &
#                you will have to answer questions based on the input image
#                """

# if submit:
#     image_data = input_image_setup(uploaded_file)
#     response=get_gemeni_response(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)
