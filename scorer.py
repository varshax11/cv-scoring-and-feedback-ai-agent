from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def score_resume(text):
    labels = ['Python', 'Machine Learning', 'AI', 'Web Development', 'Data Analysis']
    result = classifier(text, labels)
    top_skill = result['labels'][0]
    confidence = round(result['scores'][0] * 100, 2)
    batch_year = "2023" 
    ai_experience = "Yes" if "AI" in result['labels'] else "No"
    
    return {
        "Top Skill": top_skill,
        "Confidence": confidence,
        "Batch Year": batch_year,
        "AI Experience": ai_experience,
        "Overall CV Score": (confidence + (10 if ai_experience == "Yes" else 0))
    }
