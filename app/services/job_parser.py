from app.models.job_description import JobDescription
from app.services.skill_extractor import extract_skills


def parse_job_description(text: str):

    job = JobDescription()

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if lines:
        job.title = lines[0]

    job.skills = extract_skills(text)

    job.raw_text = text

    return job