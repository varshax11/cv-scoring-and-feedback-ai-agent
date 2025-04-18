![alt text](http://url/to/img.png)

# 🤖 Automated CV Scoring and Feedback AI Agent

This project automates the process of evaluating resumes, scoring them based on job relevance, and sending personalized feedback emails to candidates.

---

## 📌 Features

- 📥 Collect resumes (PDF/DOCX) from a specified folder
- 🧠 Score resumes using NLP and ML based on:
  - Education
  - Work experience
  - Skillset
  - Relevance to Job Description (JD)
- 📊 Outputs include:
  - Masked Name & Email
  - Batch year
  - Relevant AI experience
  - JD-CV Match Score
  - Total Resume Score
- 📧 Automatically sends a personalized email to the candidate with score and feedback

---

## 🛠️ Tech Stack

- **Language:** Python
- **NLP:** spaCy, NLTK, Transformers
- **AI Agent Framework:** [CrewAI](https://github.com/joaomdmoura/crewAI)
- **PDF & DOCX Parsing:** PyPDF2, docx2txt
- **Email Automation:** smtplib, email-validator

---

## 📁 Folder Structure

