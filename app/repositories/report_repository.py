from datetime import datetime

from bson import ObjectId

from app.database.database import reports_collection


class ReportRepository:

    def save_report(

        self,

        user_email,

        resume_name,

        original_filename,

        result

    ):

        candidate = result.get("candidate", {})

        report = {

            "user_email": user_email,

            "resume_name": resume_name,

            "original_filename": original_filename,

            "overall_score": result["overall_score"],

            "semantic_score": result["semantic_score"],

            "required_skill_score": result["required_skill_score"],

            "ats_score": result["ats_score"],

            "skills": result.get("skills", []),

            "matched_skills": result["matched_skills"],

            "missing_skills": result["missing_skills"],

            "feedback": result["feedback"],

            "recommendation": result.get("recommendation", ""),

            "created_at": datetime.utcnow(),

            "candidate_name": candidate.get("name", "Unknown"),

            "email": candidate.get("email", ""),

            "phone": candidate.get("phone", "")

        }

        reports_collection.insert_one(report)

    def get_reports(

        self,

        user_email

    ):

        return list(

            reports_collection.find(

                {

                    "user_email": user_email

                }

            ).sort(

                "created_at",

                -1

            )

        )

    def delete_report(

        self,

        report_id

    ):

        reports_collection.delete_one(

            {

                "_id": report_id

            }

        )

    def get_total_reports(self, email):

        return reports_collection.count_documents(

            {"user_email": email}

        )

    def get_average_match(self, email):

        pipeline = [

            {"$match": {"user_email": email}},

            {"$group": {

                "_id": None,

                "avg": {"$avg": "$overall_score"}

            }}

        ]

        result = list(reports_collection.aggregate(pipeline))

        return round(result[0]["avg"]) if result else 0

    def compare_reports(self, report_ids):

        reports = list(

            reports_collection.find(

                {

                    "_id": {

                        "$in": [

                            ObjectId(i)

                            for i in report_ids

                        ]

                }

            }

        ))

        return reports

    def get_report_by_id(self, report_id):

        return reports_collection.find_one(

            {

                "_id": ObjectId(report_id)

            }

        )

    def get_highest_match(self, email):

        pipeline = [

            {"$match": {"user_email": email}},

            {"$group": {

                "_id": None,

                "max": {"$max": "$overall_score"}

            }}

        ]

        result = list(reports_collection.aggregate(pipeline))

        return result[0]["max"] if result else 0

    def get_average_ats(self, email):

        pipeline = [

            {"$match": {"user_email": email}},

            {"$group": {

                "_id": None,

                "avg": {"$avg": "$ats_score"}

            }}

        ]

        result = list(reports_collection.aggregate(pipeline))

        return round(result[0]["avg"]) if result else 0