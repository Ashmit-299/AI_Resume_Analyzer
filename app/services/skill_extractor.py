from pathlib import Path

SKILLS_FILE = Path("data/skills.txt")

with open(SKILLS_FILE, "r", encoding="utf-8") as file:
    SKILLS = [line.strip() for line in file if line.strip()]


def extract_skills(text: str):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)

    return sorted(set(found))