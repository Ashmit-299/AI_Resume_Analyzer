from app.services.pdf import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.resume_parser import parse_resume
from app.services.ats_analyzer import analyze_ats
from app.services.job_parser import parse_job_description
from app.models.embedding_model import generate_embedding
from app.services.similarity import calculate_similarity
from app.services.skill_gap_analyzer import analyze_skill_gap
from app.services.scoring_service import ScoringService
from datetime import datetime
from app.database.database import reports_collection


class ResumeAnalysisService:

    def __init__(self):
        self.scoring = ScoringService()

    def analyze(self, pdf_path: str, job_description: str):

        resume_text = extract_text_from_pdf(pdf_path)

        resume_text = clean_text(resume_text)

        job = parse_job_description(job_description)

        resume = parse_resume(resume_text)

        resume_embedding = generate_embedding(resume_text)

        jd_embedding = generate_embedding(job_description)

        similarity_score = calculate_similarity(
            resume_embedding,
            jd_embedding
        )

        ats_report = analyze_ats(resume_text)

        skill_gap = analyze_skill_gap(resume, job)

        matched = skill_gap["matched"]
        missing = skill_gap["missing"]

        required_skill_score = self.scoring.calculate_required_skill_score(
            required_skills=matched + missing,
            resume_skills=resume.skills
        )

        overall_score = self.scoring.calculate_overall_score(
            semantic_score=similarity_score,
            required_skill_score=required_skill_score,
            ats_score=ats_report["score"]
        )

        recommendation = self._generate_recommendation(
            missing_skills=missing,
            matched_skills=matched,
            ats_feedback=ats_report["feedback"],
            overall_score=overall_score,
            ats_score=ats_report["score"],
            resume_text=resume_text,
            job_description=job_description
        )

        return {
            "candidate": {
                "name": resume.name,
                "email": resume.email,
                "phone": resume.phone,
            },
            "overall_score": overall_score,
            "semantic_score": round(similarity_score, 2),
            "required_skill_score": required_skill_score,
            "ats_score": ats_report["score"],
            "skills": resume.skills,
            "matched_skills": matched,
            "missing_skills": missing,
            "feedback": ats_report["feedback"],
            "recommendation": recommendation,
        }

    def _generate_recommendation(
        self,
        missing_skills,
        matched_skills,
        ats_feedback,
        overall_score,
        ats_score,
        resume_text,
        job_description
    ):
        recommendations = []

        if missing_skills:
            skill_list = ", ".join(missing_skills[:5])
            more = f" and {len(missing_skills) - 5} more" if len(missing_skills) > 5 else ""
            recommendations.append(
                f"Add these missing skills to your resume: {skill_list}{more}. "
                f"Include them in a dedicated 'Skills' section and demonstrate them through project descriptions or work experience."
            )

            for skill in missing_skills[:3]:
                recommendations.append(
                    f"Highlight your experience with {skill}. If you have used it in any project, "
                    f"add a bullet point describing what you built and the impact it had."
                )

        if ats_feedback:
            for item in ats_feedback:
                section = item.replace("Missing or unclear: ", "")
                if section == "Email":
                    recommendations.append(
                        "Add a professional email address at the top of your resume. "
                        "Use a format like firstname.lastname@email.com."
                    )
                elif section == "Phone":
                    recommendations.append(
                        "Include a phone number with country code at the top of your resume "
                        "for recruiters to contact you easily."
                    )
                elif section == "Education":
                    recommendations.append(
                        "Add an 'Education' section listing your degree, university, "
                        "graduation year, and relevant coursework or GPA if strong."
                    )
                elif section == "Experience":
                    recommendations.append(
                        "Add a 'Work Experience' or 'Professional Experience' section "
                        "with at least 2-3 bullet points per role describing your achievements and impact."
                    )
                elif section == "Skills":
                    recommendations.append(
                        "Create a dedicated 'Skills' section listing your technical and "
                        "soft skills. Group them by category if you have many."
                    )
                elif section == "Projects":
                    recommendations.append(
                        "Add a 'Projects' section with 2-3 projects. For each project, "
                        "include the project name, technologies used, your role, and measurable outcomes."
                    )

        if overall_score < 40:
            recommendations.append(
                "Your resume has a low match score. Consider rewriting your resume "
                "to directly address the job description. Use keywords from the JD "
                "and tailor your experience to the role."
            )
        elif overall_score < 70:
            recommendations.append(
                "Your resume is a moderate match. To improve, focus on the missing skills "
                "and ensure your experience clearly demonstrates the required competencies."
            )
        else:
            recommendations.append(
                "Your resume is a strong match for this role. Make minor adjustments "
                "to ensure all required skills are clearly highlighted."
            )

        if ats_score < 70:
            recommendations.append(
                "Your ATS score is low. Ensure your resume has clear section headings "
                "(Education, Experience, Skills, Projects), uses standard formatting, "
                "and avoids graphics or tables that ATS systems cannot parse."
            )

        if not recommendations:
            recommendations.append(
                "Your resume looks well-aligned with this job description. "
                "Continue tailoring your resume for each application to maximize your chances."
            )

        return recommendations
