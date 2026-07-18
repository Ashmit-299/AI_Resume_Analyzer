from app.services.pdf import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.resume_parser import parse_resume
from app.services.ats_analyzer import analyze_ats

from app.models.embedding_model import generate_embedding
from app.services.similarity import calculate_similarity


class ResumeAnalysisService:

    def analyze(self, pdf_path: str, job_description: str):

        resume_text = extract_text_from_pdf(pdf_path)

        resume_text = clean_text(resume_text)

        resume = parse_resume(resume_text)

        resume_embedding = generate_embedding(resume_text)

        jd_embedding = generate_embedding(job_description)

        similarity_score = calculate_similarity(
            resume_embedding,
            jd_embedding
        )

        ats_report = analyze_ats(resume_text)

        return resume, similarity_score, ats_report