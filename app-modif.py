import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_PRO_API_KEY"))

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = " ".join([page.extract_text() or "" for page in reader.pages])
    return text.strip()

# Function to get response from Gemini API
def get_gemini_response(resume_text, job_description):
    model = genai.GenerativeModel('gemini-2.0-flash')
    input_prompt = f"""
    Act as an **advanced Applicant Tracking System (ATS)** specialized in **Software Engineering, Data Science, and Big Data Engineering**.
    Evaluate the resume against the provided job description, considering a **highly competitive job market**.
    Provide an ATS-style evaluation with **high accuracy**, listing missing keywords and percentage match.

    📌 **Expected Response Format (STRICT JSON FORMAT, NO EXTRA TEXT)**:
    ```json
    {{
        "JD Match": "XX%",
        "MissingKeywords": ["keyword1", "keyword2"],
        "Profile Summary": "..."
    }}
    ```
    ❗ **IMPORTANT:**  
    - **Return ONLY valid JSON** (no extra comments, explanations, or markdown).  
    - **Do NOT include escape characters** (`\n`, `\t`, etc.).  
    - **Do NOT include text before or after the JSON output.**  
    - **Ensure all percentage values contain `%` (e.g., `"85%"`).**

    **Resume Content:**
    {resume_text}

    **Job Description:**
    {job_description}
    """

    response = model.generate_content(input_prompt)
    return response.text

# Function to clean and validate JSON response
def clean_and_parse_json(response_text):
    try:
        # Extract only valid JSON using regex
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            cleaned_json = json_match.group(0)  # Get valid JSON content
            return json.loads(cleaned_json)
        else:
            return None
    except json.JSONDecodeError:
        return None

# Streamlit UI
st.set_page_config(page_title="Smart ATS - Resume Evaluator", layout="centered", page_icon="📄")
st.title("📄 Smart ATS - Resume Evaluator")
st.markdown("🚀 **Optimize your resume for Applicant Tracking Systems (ATS) & boost your job search success!**")

# Input Section
jd = st.text_area("📌 Paste the Job Description Below", height=150)
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type="pdf", help="Upload your resume in PDF format.")
submit = st.button("✨ Analyze Resume")

if submit:
    if uploaded_file and jd:
        with st.spinner("Analyzing Resume... 🕵️‍♂️"):
            resume_text = input_pdf_text(uploaded_file)
            response_text = get_gemini_response(resume_text, jd)
            response_data = clean_and_parse_json(response_text)

            if response_data:
                match_percentage = response_data.get("JD Match", "0%")
                missing_keywords = response_data.get("MissingKeywords", [])
                profile_summary = response_data.get("Profile Summary", "No summary provided.")

                # Display results
                st.subheader("✅ ATS Evaluation Results")
                st.progress(int(match_percentage.replace("%", "")) / 100)
                st.write(f"💡 **Your resume matches {match_percentage} with the job description.**")

                if missing_keywords:
                    st.subheader("❌ Missing Keywords")
                    st.markdown(" ".join([f"`{word}`" for word in missing_keywords]))
                else:
                    st.success("✅ No critical keywords missing!")

                with st.expander("📌 Profile Summary"):
                    st.markdown(f"**{profile_summary}**")
            else:
                st.error("⚠️ Failed to process the response. Gemini did not return valid JSON.")
                st.code(response_text, language="json")

    else:
        st.warning("⚠️ Please upload a resume and enter the job description.")
