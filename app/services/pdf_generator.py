from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    HRFlowable, Table, TableStyle
)


class PDFGenerator:

    def __init__(self):
        self.output_dir = Path("uploads")
        self.output_dir.mkdir(exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._setup_styles()

    def _setup_styles(self):
        self.title_style = ParagraphStyle(
            "ReportTitle",
            parent=self.styles["Heading1"],
            fontSize=22,
            spaceAfter=20,
            textColor=colors.HexColor("#1F2937"),
        )
        self.section_style = ParagraphStyle(
            "SectionTitle",
            parent=self.styles["Heading2"],
            fontSize=14,
            spaceBefore=16,
            spaceAfter=8,
            textColor=colors.HexColor("#2563EB"),
        )
        self.normal_style = ParagraphStyle(
            "CustomNormal",
            parent=self.styles["Normal"],
            fontSize=11,
            leading=16,
        )
        self.footer_style = ParagraphStyle(
            "Footer",
            parent=self.styles["Normal"],
            fontSize=9,
            textColor=colors.HexColor("#9CA3AF"),
            alignment=1,
        )

    def generate_report(self, data: dict) -> Path:
        candidate_name = data.get("candidate", {}).get("name") or "candidate"
        safe_name = candidate_name.replace(" ", "_").replace("/", "_")
        filename = f"report_{safe_name}.pdf"
        pdf_path = self.output_dir / filename

        doc = SimpleDocTemplate(
            str(pdf_path),
            pagesize=A4,
            rightMargin=0.6 * inch,
            leftMargin=0.6 * inch,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch,
        )

        story = []

        self._add_title(story, data)
        self._add_candidate_info(story, data)
        self._add_scores(story, data)
        self._add_skills(story, data)
        self._add_matched_skills(story, data)
        self._add_missing_skills(story, data)
        self._add_ats_feedback(story, data)
        self._add_recommendations(story, data)
        self._add_footer(story)

        doc.build(story)
        return pdf_path

    def _add_title(self, story, data):
        story.append(
            Paragraph("TalentLens AI — Candidate Report", self.title_style)
        )
        story.append(
            HRFlowable(width="100%", color=colors.HexColor("#2563EB"))
        )
        story.append(Spacer(1, 0.2 * inch))

    def _add_candidate_info(self, story, data):
        story.append(Paragraph("Candidate Information", self.section_style))
        c = data["candidate"]
        story.append(Paragraph(f"<b>Name:</b> {c['name']}", self.normal_style))
        story.append(Paragraph(f"<b>Email:</b> {c['email']}", self.normal_style))
        story.append(Paragraph(f"<b>Phone:</b> {c['phone']}", self.normal_style))
        story.append(Spacer(1, 0.15 * inch))

    def _add_scores(self, story, data):
        story.append(Paragraph("Scores", self.section_style))
        story.append(
            Paragraph(
                f"<b>Overall Match:</b> {data['overall_score']}%",
                self.normal_style,
            )
        )
        story.append(
            Paragraph(
                f"<b>Semantic Match:</b> {data['semantic_score']}%",
                self.normal_style,
            )
        )
        story.append(
            Paragraph(
                f"<b>Required Skill Coverage:</b> {data['required_skill_score']}%",
                self.normal_style,
            )
        )
        story.append(
            Paragraph(
                f"<b>ATS Score:</b> {data['ats_score']}/100",
                self.normal_style,
            )
        )
        story.append(Spacer(1, 0.15 * inch))

    def _add_skills(self, story, data):
        story.append(Paragraph("Detected Skills", self.section_style))
        for skill in data["skills"]:
            story.append(
                Paragraph(
                    f'<font color="#10B981">✓</font> {skill}',
                    self.normal_style,
                )
            )
        story.append(Spacer(1, 0.1 * inch))

    def _add_matched_skills(self, story, data):
        story.append(Paragraph("Matched Skills", self.section_style))
        for skill in data["matched_skills"]:
            story.append(
                Paragraph(
                    f'<font color="#10B981">✓</font> {skill}',
                    self.normal_style,
                )
            )
        story.append(Spacer(1, 0.1 * inch))

    def _add_missing_skills(self, story, data):
        story.append(Paragraph("Missing Skills", self.section_style))
        for skill in data["missing_skills"]:
            story.append(
                Paragraph(
                    f'<font color="red">✗</font> {skill}',
                    self.normal_style,
                )
            )
        story.append(Spacer(1, 0.1 * inch))

    def _add_ats_feedback(self, story, data):
        if not data.get("feedback"):
            return
        story.append(Paragraph("ATS Suggestions", self.section_style))
        for item in data["feedback"]:
            recommendation = "Suggestion"
            message = item
            box = Table(
                [[recommendation, message]],
                colWidths=[140, 300],
            )
            box.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F3F4F6")),
                        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#2563EB")),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 15),
                        ("TOPPADDING", (0, 0), (-1, -1), 15),
                        ("FONTNAME", (0, 0), (0, 0), "Helvetica-Bold"),
                    ]
                )
            )
            story.append(box)
            story.append(Spacer(1, 0.1 * inch))

    def _add_recommendations(self, story, data):
        recommendations = data.get("recommendation", [])
        if not recommendations:
            return
        story.append(Paragraph("Recommendations to Get Shortlisted", self.section_style))
        for rec in recommendations:
            story.append(
                Paragraph(
                    f'<font color="#22C55E">→</font> {rec}',
                    self.normal_style,
                )
            )
            story.append(Spacer(1, 0.05 * inch))
        story.append(Spacer(1, 0.1 * inch))

    def _add_footer(self, story):
        story.append(Spacer(1, 0.4 * inch))
        story.append(
            HRFlowable(width="100%", color=colors.grey)
        )
        story.append(Spacer(1, 0.1 * inch))
        story.append(
            Paragraph(
                "Generated by TalentLens AI",
                self.footer_style,
            )
        )
        story.append(
            Paragraph(
                "AI Recruitment Assistant",
                self.footer_style,
            )
        )
        story.append(
            Paragraph(
                "© 2026 Ashmit Pandey",
                self.footer_style,
            )
        )
