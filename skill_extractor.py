skills_db = [

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "aws",
    "docker",
    "fastapi",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "langchain",
    "rag",
    "streamlit"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found