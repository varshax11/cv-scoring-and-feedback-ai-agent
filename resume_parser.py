import spacy
import docx2txt
import PyPDF2
import re

spacy_model = spacy.load("en_core_web_sm")

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    return ""

def mask_info(text):
    doc = spacy_model(text)
    name, email = "", ""
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        if ent.label_ == "EMAIL" and not email:
            email = ent.text
    masked_name = "Candidate"
    masked_email = email.replace("@", "[at]").replace(".", "[dot]") if email else "unknown[at]email[dot]com"
    return masked_name, masked_email

def extract_resume_info(file_path):
    text = extract_text(file_path)
    name, email = mask_info(text)
    return text, name, email