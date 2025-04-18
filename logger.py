import csv
import os

def log_process(name, score_data):
    logfile = 'logs/processed_resumes.csv'
    header = ['Name', 'Top Skill', 'Confidence', 'Batch Year', 'AI Experience', 'Overall CV Score']
    
    file_exists = os.path.isfile(logfile)
    with open(logfile, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'Name': name,
            **score_data
        })