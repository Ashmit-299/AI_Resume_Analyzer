import re

from app.models.resume import Resume
from app.services.skill_extractor import extract_skills

def parse_resume(text: str) -> Resume:

    resume = Resume()

    email = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text,
    )

    if email:
        resume.email = email.group()

    phone = re.search(
        r"\+?\d[\d\s\-]{8,15}",
        text,
    )

    if phone:
        resume.phone = phone.group()

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    
    github = re.search(
    r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+",
    text,
    re.IGNORECASE,
)

    if github:
        resume.github = github.group()
        
    linkedin = re.search(
    r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
    text,
    re.IGNORECASE,
)

    if linkedin:
        resume.linkedin = linkedin.group()

    if lines:
        resume.name = lines[0]

    resume.skills = extract_skills(text)

    resume.raw_text = text

    return resume