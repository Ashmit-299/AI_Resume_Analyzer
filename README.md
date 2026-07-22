# 🚀 TalentLens AI

<p align="center">

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/747c60f707976e37e8ab0a72b6ee9fd1a2a0ecc0/assets/TalentLens%20AI.png)

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

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Login%20Page.png)

---

## Landing Page

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Landing%20Page.png)

---

## Resume Upload

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Resume%20Upload.png)

---

## AI Processing

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/AI%20Processing.png)

---

## Analysis Result

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Analysis%20Result%20-%201.png)

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Analysis%20Result%20-%202.png)

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Analysis%20Result%20-%203.png)

---

## Final Report

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Final%20Report%20-%201.png)

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Final%20Report%20-%202.png)

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/Final%20Report%20-%203.png)

## About

![image alt](https://github.com/Ashmit-299/AI_Resume_Analyzer/blob/e1f1ac30f0e7009bd5c672ee1eeb37eb3773e0e2/assets/About.png)

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
