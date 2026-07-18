from app.services.resume_analysis_service import ResumeAnalysisService
from app.services.report_generator import print_report


job_description = """
Looking for an AI Engineer.

Required Skills:
Python
SQL
TensorFlow
Docker
AWS
Git
"""


service = ResumeAnalysisService()

resume, score, ats = service.analyze(
    "Ashmit_Data_Analytics_Resume.pdf",
    job_description,
)

print_report(
    score,
    ats,
    resume
)