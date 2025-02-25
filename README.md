# Gemini-ATS-Resume-Tracker
Model utilizes Google’s Gemini (gemini-1.5-flash) generative model to deliver accurate and actionable feedback.
Gemini ATS Resume Tracker
An end-to-end resume evaluation and skill enhancement tool built with Streamlit and powered by Google's Gemini model (gemini-1.5-flash). This application leverages advanced AI capabilities to analyze resumes against job descriptions, provide actionable insights, and generate an ATS match score to help job seekers optimize their profiles.

Project Description
Gemini ATS Resume Tracker is an intelligent system designed to assist both candidates and recruiters in the hiring process. The application allows users to upload a resume (in PDF format) and enter a job description. Powered by Google's generative AI model (gemini-1.5-flash), the system provides:

Resume Evaluation: A professional assessment highlighting the strengths and weaknesses of the candidate's profile relative to the job requirements.
Skill Improvement Guidance: Actionable recommendations for skill enhancement, including courses, certifications, and practical projects to bridge any identified gaps.
ATS Matching Score: An ATS-friendly match score that includes a percentage match, missing keywords, and a concise final assessment, helping candidates optimize their resumes for better job market alignment.
The project combines several powerful tools and libraries, including Streamlit for the web interface, pdf2image for PDF processing, and Pillow for image handling. Additionally, environment management is streamlined via python-dotenv, ensuring that sensitive API keys remain secure.

Features
Resume Upload: Easily upload a PDF resume.
Job Description Input: Paste the desired job description for targeted analysis.
AI-Driven Insights:
Resume Evaluation: Get a professional review of your resume.
Skill Enhancement Advice: Learn how to improve your profile with industry-specific recommendations.
ATS Match Score: Understand your resume’s compatibility with the job posting via a match percentage and keyword analysis.
Powered by Gemini: Utilizes Google’s Gemini (gemini-1.5-flash) generative model to deliver accurate and actionable feedback.
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.7 or higher
pip
Poppler (required for pdf2image)
Windows: Download and add the Poppler bin folder to your PATH.
macOS: brew install poppler
Linux: sudo apt-get install poppler-utils
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/gemini-ats-resume-tracker.git
cd gemini-ats-resume-tracker
Create a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Set up Environment Variables:

Create a .env file in the root directory and add your Google API key:

ini
Copy
Edit
GOOGLE_PRO_API_KEY=your_google_pro_api_key_here
Usage
Run the Streamlit application:

bash
Copy
Edit
streamlit run app.py
Interact with the App:

Enter the job description in the provided text area.
Upload your resume in PDF format.
Use one of the buttons to:
Tell Me About The Resume: Receive a professional evaluation of your resume.
How Can I Upgrade my Skills: Get recommendations for skill enhancement.
Percentage Match of The Resume: Get an ATS match score including missing keywords and a final assessment.
Code Overview
app.py: Main Streamlit application that handles UI interactions, PDF processing, and calls to the Gemini model.
Functions:
input_pdf_setup(uploaded_file): Converts the first page of the uploaded PDF into a base64 encoded JPEG image.
get_gemini_response(input, pdf_content, prompt): Sends the job description, processed PDF content, and a specific prompt to the Gemini model to generate a response.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any feature requests or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Streamlit for an amazing framework to build interactive web applications.
Google Generative AI for powering the intelligent resume analysis.
pdf2image and Pillow for handling PDF and image processing.
