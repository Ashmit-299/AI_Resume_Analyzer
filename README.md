# 🚀 TalentLens AI

<p align="center">

![image alt]()

</p>

<h3 align="center">
AI-Powered Resume Analysis & Recruitment Assistant
</h3>

<p align="center">

Analyze resumes using Artificial Intelligence, Semantic Search, ATS Scoring, Skill Gap Detection, and Intelligent Candidate Matching.

</p>

---

## 📌 Overview

TalentLens AI is an AI-powered recruitment platform that helps recruiters, HR professionals, and job seekers evaluate resumes against job descriptions.

Instead of relying only on keyword matching, TalentLens AI combines Natural Language Processing (NLP), Sentence Transformers, ATS Scoring, and Skill Gap Analysis to understand the actual meaning of a resume and compare it with the required job profile.

The system also provides an intuitive dashboard, downloadable PDF reports, Google Authentication, resume history, and candidate comparison.

---

# ✨ Features

✅ Google Authentication

- Secure Google OAuth Login
- Session-based Authentication

---

✅ Resume Parsing

- Upload PDF Resume
- Extract Resume Text
- Parse Candidate Information

---

✅ AI Resume Analysis

- Semantic Similarity
- Required Skills Detection
- Missing Skills Detection
- ATS Score
- Overall Match Score

---

✅ Dashboard

- Beautiful Landing Page
- Resume Upload
- Job Description Input
- AI Analysis
- Animated Processing Screen

---

✅ Reports

- Download PDF Report
- Resume History
- Candidate Comparison

---

✅ Database

- MongoDB Atlas
- Stores Users
- Stores Analysis Reports

---

# 🧠 AI Pipeline

```text
Resume PDF
      │
      ▼
Text Extraction
      │
      ▼
Cleaning
      │
      ▼
Sentence Transformer Embedding
      │
      ▼
Job Description Embedding
      │
      ▼
Semantic Similarity
      │
      ▼
Skill Extraction
      │
      ▼
ATS Score
      │
      ▼
Overall Score
      │
      ▼
PDF Report
```

---

# 📷 Screenshots

## Login Page

![image alt]()

---

## Landing Page

![image alt]()

---

## Resume Upload

![image alt]()

---

## AI Processing

![image alt]()

---

## Analysis Result

![image alt]()

---

## Final Report

![image alt]()

---

# 🏗 Project Structure

```
TalentLens-AI
│
├── app
│   ├── api
│   ├── auth
│   ├── config
│   ├── database
│   ├── repositories
│   ├── routers
│   ├── services
│   ├── templates
│   ├── static
│   └── main.py
│
├── uploads
├── reports
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- Uvicorn

---

## AI

- Sentence Transformers
- Transformers
- Scikit Learn

---

## Database

- MongoDB Atlas

---

## Authentication

- Google OAuth
- Authlib
- Session Middleware

---

## Frontend

- HTML
- CSS
- JavaScript

---

## PDF

- ReportLab

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/Ashmit-299/AI_Resume_Analyzer.git
```

Go inside project

```bash
cd TalentLens-AI
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run project

```bash
uvicorn app.main:app --reload
```

Open browser

```
http://127.0.0.1:8000
```

---

# 🔐 Environment Variables

Create

```
.env
```

```
MONGODB_URI=

DATABASE_NAME=

GOOGLE_CLIENT_ID=

GOOGLE_CLIENT_SECRET=

SECRET_KEY=
```

---

# 📊 Score Calculation

Overall Score

```
Overall Score

=

50% Required Skills

+

30% Semantic Similarity

+

20% ATS Score
```

---

# 🗂 Database Collections

Users

```
users
```

Stores

- Name
- Email
- Google ID
- Profile Picture
- Login Time

Reports

```
reports
```

Stores

- Resume
- Job Description
- Scores
- Skills
- PDF Path
- Created Time

---

# 🚀 Deployment

Deployment Platform

- Render

Database

- MongoDB Atlas

Authentication

- Google OAuth

---

# 📈 Future Improvements

- AI Interview Questions
- Resume Ranking
- Recruiter Dashboard
- Company Portal
- Email Reports
- Resume Recommendations
- Multi-language Support

---

# 👨‍💻 Author

**Ashmit Pandey**

Artificial Intelligence & Machine Learning Engineer

GitHub

```
https://github.com/Ashmit-299
```

LinkedIn

```
www.linkedin.com/in/ashmit299
```

Email

```
pandeyashmit299@gmail.com
```

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.