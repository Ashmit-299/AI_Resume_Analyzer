import re


class ScoringService:

    def calculate_required_skill_score(
        self,
        required_skills,
        resume_skills
    ):

        if not required_skills:
            return 100.0

        resume = {

            skill.lower()

            for skill in resume_skills

        }

        matched = [

            skill

            for skill in required_skills

            if skill.lower() in resume

        ]

        score = (

            len(matched)

            / len(required_skills)

        ) * 100

        return round(score, 2)

    def calculate_overall_score(

        self,

        semantic_score,

        required_skill_score,

        ats_score

    ):

        overall = (

            0.50 * required_skill_score +

            0.30 * semantic_score +

            0.20 * ats_score

        )

        return round(overall, 2)
