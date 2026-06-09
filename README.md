# AI Resume Screener & Candidate Ranking System

# AI Resume Screener & Candidate Ranking System

🚀 Live Demo:
https://ai-resume-screener-mengrjxtcqmb4senfxq9ps.streamlit.app/

📂 Source Code:
https://github.com/So050602/ai-resume-screener

---

## Overview

AI Resume Screener is an intelligent candidate evaluation platform that automates resume screening, skill-gap analysis, and candidate ranking against a given Job Description (JD).

The system leverages Natural Language Processing (NLP), Sentence Transformer embeddings, semantic similarity matching, and ATS-style scoring to identify the most suitable candidates for a role. It also generates candidate insights, hiring recommendations, and interview questions to assist recruiters during the shortlisting process.

---

## Key Features

### Resume Processing

* Upload multiple resume PDFs
* Upload a Job Description (JD) PDF
* Automatic resume text extraction

### NLP & Semantic Analysis

* Resume preprocessing and text normalization
* Skill extraction from resumes and job descriptions
* Transformer-based sentence embeddings
* Semantic similarity matching using cosine similarity

### ATS Candidate Evaluation

* ATS-style candidate scoring
* Skill-gap identification
* Candidate ranking engine
* Top candidate recommendation

### AI Candidate Intelligence

* Candidate strengths identification
* Missing skills detection
* Hiring recommendation generation
* Technical interview question generation

### Recruiter Dashboard

* Interactive Streamlit interface
* Candidate ranking table
* ATS score visualization
* Downloadable ranking report

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### NLP & Deep Learning

* Sentence Transformers (all-MiniLM-L6-v2)
* Transformers
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### PDF Processing

* PyPDF2
* pdfplumber

---

## System Workflow

1. Upload Job Description PDF
2. Upload Candidate Resume PDFs
3. Extract text from uploaded documents
4. Generate semantic embeddings using Sentence Transformers
5. Compute cosine similarity between resumes and JD
6. Extract and compare skills
7. Calculate ATS-style scores
8. Rank candidates based on relevance
9. Generate candidate analysis and recommendations
10. Present recruiter-friendly dashboard

---

## Machine Learning Concepts Used

* Cosine Similarity
* Semantic Search
* Skill Matching
* Text Similarity Analysis
* ATS Score Computation

---

## Deep Learning Concepts Used

* Sentence Embeddings
* Transformer-based NLP
* Semantic Text Matching

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Output

For each candidate, the system provides:

* ATS Score
* Semantic Similarity Score
* Matched Skills
* Missing Skills
* Hiring Recommendation
* Candidate Strengths
* Technical Interview Questions

---

## Future Scope

* LLM-powered candidate analysis
* FAISS vector search
* Multi-job comparison
* Recruiter analytics dashboard
* Cloud deployment
* Multi-language resume processing

---

## Project Outcome

This project demonstrates the practical application of:

* Natural Language Processing (NLP)
* Deep Learning for semantic matching
* Transformer-based text embeddings
* ATS automation
* Resume intelligence systems
* End-to-end AI application development
