from config import EMAIL_ADDRESS, EMAIL_PASSWORD
from resume_parser import extract_resume_info
from scorer import score_resume
from email_sender import send_feedback_email
from logger import log_process

import os
from crewai import Agent, Task, Crew

def main():
    print("Starting Automated CV Scoring System")

    resume_folder = 'resumes'
    if not os.path.exists(resume_folder):
        print(f"Resume folder '{resume_folder}' not found.")
        return

    resumes = [os.path.join(resume_folder, f) for f in os.listdir(resume_folder) if f.endswith(('.pdf', '.docx'))]
    if not resumes:
        print("No resumes found in the folder.")
        return

    extractor_agent = Agent(role="Extractor", goal="Extract resume details", backstory="Expert at parsing resumes.")
    scorer_agent = Agent(role="Scorer", goal="Score resumes", backstory="Evaluates resumes for AI experience.")
    email_agent = Agent(role="Email Sender", goal="Send feedback emails", backstory="Handles communication.")
    logger_agent = Agent(role="Logger", goal="Log resume processing", backstory="Tracks processed resumes.")

    crew = Crew(agents=[extractor_agent, scorer_agent, email_agent, logger_agent], tasks=[], verbose=True)

    for resume_path in resumes:
        print(f"\n Processing: {os.path.basename(resume_path)}")

        text, candidate_name, real_email = extract_resume_info(resume_path)

        if not real_email:
            print(f"Email not found in {resume_path}, skipping...")
            continue

        score_data = score_resume(text)

        send_feedback_email(real_email, candidate_name, score_data)

        log_process(candidate_name, score_data)

    print("\n All resumes processed and feedback sent!")


if __name__ == "__main__":
    main()
