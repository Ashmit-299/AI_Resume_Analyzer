import re

def analyze_ats(resume_text: str):
    score = 100
    feedback = []

    text = resume_text.lower()

    checks = {
        "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "Phone": r"\+?\d[\d\s-]{8,}",
        "Education": r"\beducation\b",
        "Experience": r"\bexperience\b",
        "Skills": r"\bskills\b",
        "Projects": r"\bprojects?\b",
    }

    for section, pattern in checks.items():
        if not re.search(pattern, text):
            score -= 10
            feedback.append(f"Missing or unclear: {section}")

    score = max(score, 0)

    return {
        "score": score,
        "feedback": feedback
    }