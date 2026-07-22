def analyze_skill_gap(resume, job):

    matched = []
    missing = []

    resume_skills = {skill.lower() for skill in resume.skills}

    for skill in job.skills:

        if skill.lower() in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return {
        "matched": sorted(matched),
        "missing": sorted(missing)
    }