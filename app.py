from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_PRO_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

#STREAMLIT APP
st.set_page_config(page_title="ATS Resume Tracker")
st.header("Gemini ATS Tracking System ")
input_text=st.text_area("Job Description:", key="input")
uploaded_file=st.file_uploader("Upload your resume (PDF) ...",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Succesfully")
submit1 = st.button("Tell Me About The Resume")
submit2 = st.button("How Can I Upgrade my Skills")
submit3 = st.button("Percentage Match of The Resume")


input_prompt1 = """
You are a highly experienced **Technical Human Resource Manager** with expertise in talent acquisition and job fit analysis.  
Your task is to **evaluate the provided resume** against the given job description and provide a **professional assessment** of the candidate's suitability.  

 **Key Focus Areas:**  
- Identify **strengths** that align with the job role.  
- Highlight **weaknesses** or skill gaps.  
- Assess **how well the candidate fits the role** based on their experience, skills, and qualifications.  

Provide an insightful, structured evaluation in a clear and professional tone.
"""

input_prompt2 = """
You are an **HR and Career Development Specialist** with deep knowledge of industry trends and skill-building strategies.  
Your task is to **analyze the provided resume** and recommend tailored **skill improvement strategies** based on the job description.  

 **Key Focus Areas:**  
- Identify missing **technical and soft skills** required for the role.  
- Suggest relevant **courses, certifications, or hands-on projects** to bridge skill gaps.  
- Provide industry-specific **growth strategies** to enhance the candidate’s career prospects.  

Offer actionable insights that help the candidate **strengthen their profile** and increase their job market value.
"""


input_prompt3 = """
You are an **advanced ATS (Applicant Tracking System) scanner** with deep expertise in **resume parsing and job matching algorithms**.  
Your task is to analyze the resume against the provided job description and return a **structured ATS match score**.

 **Output Format:**  
 **Match Percentage:** Provide an overall **match score** (e.g., "78% Match") based on keyword relevance and experience fit.  
 **Missing Keywords:** List any **important skills, qualifications, or job-specific terms** that the resume lacks.  
 **Final Assessment:** Offer a **brief conclusion** on how well the candidate fits the role and suggest **potential improvements**.  

Ensure a structured, ATS-friendly evaluation to help optimize the resume for **better job application success**.
"""


if submit1:
    if uploaded_file is not None: 
        pdf_content=input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_text,pdf_content,input_prompt1)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please Upload Your Resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_prompt2)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

else:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_prompt3)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
