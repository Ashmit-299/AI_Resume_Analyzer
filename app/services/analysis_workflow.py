import uuid
import os

from app.services.resume_analysis_service import ResumeAnalysisService
from app.repositories.report_repository import ReportRepository
from app.services.pdf_generator import PDFGenerator
from app.core.logger import logger
from app.core.exceptions import ResumeAnalysisException
from app.config.settings import settings


class AnalysisWorkflow:

    def __init__(self):

        self.analysis_service = ResumeAnalysisService()

        self.repository = ReportRepository()

        self.pdf_generator = PDFGenerator()

    def analyze_resume(self, file_content, original_filename, user_email, job_description):

        try:

            filename = f"{uuid.uuid4()}.pdf"

            file_path = os.path.join(
                settings.UPLOAD_FOLDER,
                filename
            )

            with open(file_path, "wb") as f:

                f.write(file_content)

            logger.info(f"File saved: {filename}")

            result = self.analysis_service.analyze(
                file_path,
                job_description
            )

            self.repository.save_report(
                user_email=user_email,
                resume_name=filename,
                original_filename=original_filename,
                result=result
            )

            logger.info(f"Analysis completed for {original_filename}")

            return result

        except Exception as e:

            logger.error(f"Analysis failed: {str(e)}")

            raise ResumeAnalysisException(str(e))

    def generate_report(self, data):

        try:

            pdf_path = self.pdf_generator.generate_report(data)

            logger.info("PDF report generated")

            return pdf_path

        except Exception as e:

            logger.error(f"PDF generation failed: {str(e)}")

            raise ResumeAnalysisException(str(e))
