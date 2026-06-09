def generate_ai_summary(
        resume_text,
        jd_text):

    strengths = []

    if "python" in resume_text.lower():
        strengths.append("Strong Python programming skills")

    if "machine learning" in resume_text.lower():
        strengths.append("Experience with Machine Learning")

    if "deep learning" in resume_text.lower():
        strengths.append("Hands-on Deep Learning experience")

    if "nlp" in resume_text.lower():
        strengths.append("Natural Language Processing expertise")

    if "fastapi" in resume_text.lower():
        strengths.append("Backend API development using FastAPI")

    if "streamlit" in resume_text.lower():
        strengths.append("Interactive dashboard development using Streamlit")

    if "tensorflow" in resume_text.lower():
        strengths.append("Experience with TensorFlow")

    if "pytorch" in resume_text.lower():
        strengths.append("Experience with PyTorch")

    if len(strengths) == 0:
        strengths.append("Relevant technical background identified")

    missing_skills = []

    jd_lower = jd_text.lower()
    resume_lower = resume_text.lower()

    important_skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
        "aws",
        "docker",
        "fastapi",
        "tensorflow",
        "pytorch"
    ]

    for skill in important_skills:

        if skill in jd_lower and skill not in resume_lower:

            missing_skills.append(skill.upper())

    if len(missing_skills) == 0:

        recommendation = (
            "Strong candidate. Recommended for technical interview."
        )

    elif len(missing_skills) <= 2:

        recommendation = (
            "Good candidate. Consider for technical interview."
        )

    else:

        recommendation = (
            "Candidate requires additional skill development."
        )

    summary = f"""
## Candidate Strengths

{chr(10).join([f"- {item}" for item in strengths])}

## Missing Skills

{chr(10).join([f"- {item}" for item in missing_skills]) if missing_skills else "- No major skill gaps identified"}

## Hiring Recommendation

{recommendation}

## Technical Interview Questions

1. Explain cosine similarity and how it is used in resume matching systems.

2. How do transformer-based embeddings improve semantic search?

3. Describe a machine learning project you have built and the challenges you faced.
"""

    return summary