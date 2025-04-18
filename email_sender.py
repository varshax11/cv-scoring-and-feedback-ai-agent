import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_feedback_email(to_email, name, score_data):
    msg = EmailMessage()
    msg['Subject'] = 'Your Resume Evaluation Result'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email.replace("[at]", "@").replace("[dot]", ".")
    
    content = f"""
Hi {name},

Thank you for submitting your resume.
Here’s your evaluation summary:

- Top Skill: {score_data['Top Skill']}
- Confidence Score: {score_data['Confidence']}%
- Batch Year: {score_data['Batch Year']}
- Relevant AI Experience: {score_data['AI Experience']}
- Overall CV Score: {score_data['Overall CV Score']}/100

Best wishes,
Team Elint
    """
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)