
import streamlit as st
import pandas as pd

from modules.pdf_parser import extract_text
from modules.ranking import calculate_similarity
from modules.skill_extractor import extract_skills
from modules.ai_summary import generate_ai_summary

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screener",
    layout="wide"
)

st.title("🤖 AI Resume Screener & Candidate Ranking System")

st.markdown("""
Upload a Job Description and multiple resumes.

The system will:
- Extract resume content
- Perform semantic matching
- Calculate ATS score
- Identify missing skills
- Rank candidates
- Generate AI-powered candidate analysis
""")

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "results_df" not in st.session_state:
    st.session_state.results_df = None

if "jd_text" not in st.session_state:
    st.session_state.jd_text = None

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

jd_file = st.file_uploader(
    "📄 Upload Job Description PDF",
    type=["pdf"]
)

resume_files = st.file_uploader(
    "📑 Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------

if st.button("🚀 Analyze Candidates"):

    if jd_file is None:
        st.error("Please upload a Job Description PDF.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one Resume PDF.")
        st.stop()

    with st.spinner("Processing Job Description..."):
        jd_text = extract_text(jd_file)

    jd_skills = extract_skills(jd_text)

    results = []

    with st.spinner("Analyzing Resumes..."):

        for resume in resume_files:

            resume_text = extract_text(resume)

            similarity_score = calculate_similarity(
                resume_text,
                jd_text
            )

            resume_skills = extract_skills(
                resume_text
            )

            matched_skills = list(
                set(resume_skills).intersection(
                    set(jd_skills)
                )
            )

            missing_skills = list(
                set(jd_skills) - set(resume_skills)
            )

            if len(jd_skills) > 0:

                skill_match_score = (
                    len(matched_skills)
                    / len(jd_skills)
                ) * 100

            else:

                skill_match_score = 0

            ats_score = (
                0.7 * similarity_score +
                0.3 * skill_match_score
            )

            ats_score = round(
                ats_score,
                2
            )

            if ats_score >= 75:

                recommendation = "✅ Strong Match"

            elif ats_score >= 50:

                recommendation = "🟡 Consider for Interview"

            else:

                recommendation = "❌ Weak Match"

            results.append({

                "Candidate":
                    resume.name,

                "Resume Text":
                    resume_text,

                "Similarity Score (%)":
                    round(similarity_score, 2),

                "ATS Score (%)":
                    ats_score,

                "Matched Skills":
                    ", ".join(matched_skills)
                    if matched_skills
                    else "None",

                "Missing Skills":
                    ", ".join(missing_skills)
                    if missing_skills
                    else "None",

                "Recommendation":
                    recommendation
            })

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="ATS Score (%)",
        ascending=False
    )

    df.reset_index(
        drop=True,
        inplace=True
    )

    df.insert(
        0,
        "Rank",
        range(1, len(df) + 1)
    )

    st.session_state.results_df = df
    st.session_state.jd_text = jd_text

# ---------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------

if st.session_state.results_df is not None:

    df = st.session_state.results_df
    jd_text = st.session_state.jd_text

    display_df = df.drop(
        columns=["Resume Text"]
    )

    st.divider()

    st.subheader("🏆 Candidate Rankings")

    st.dataframe(
        display_df,
        use_container_width=True
    )

    csv = display_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download Ranking Report",
        data=csv,
        file_name="candidate_rankings.csv",
        mime="text/csv"
    )

    # -------------------------
    # TOP CANDIDATE
    # -------------------------

    top_candidate = df.iloc[0]

    st.divider()

    st.subheader("🌟 Top Candidate")

    st.success(
        f"{top_candidate['Candidate']} | "
        f"ATS Score: {top_candidate['ATS Score (%)']}%"
    )

    st.metric(
        label="Top ATS Score",
        value=f"{top_candidate['ATS Score (%)']}%"
    )

    # -------------------------
    # CANDIDATE ANALYSIS
    # -------------------------

    st.divider()

    st.subheader("📊 Candidate Analysis")

    for _, row in df.iterrows():

        with st.expander(
            f"{row['Candidate']} | ATS Score: {round(row['ATS Score (%)'],2)}%"
        ):

            st.progress(
                row["ATS Score (%)"] / 100
            )

            st.write(
                f"**Semantic Similarity:** "
                f"{round(row['Similarity Score (%)'],2)}%"
            )

            st.write(
                f"**ATS Score:** "
                f"{round(row['ATS Score (%)'],2)}%"
            )

            st.write(
                f"**Matched Skills:** "
                f"{row['Matched Skills']}"
            )

            st.write(
                f"**Missing Skills:** "
                f"{row['Missing Skills']}"
            )

            matched_count = (
                len(row["Matched Skills"].split(","))
                if row["Matched Skills"] != "None"
                else 0
            )

            missing_count = (
                len(row["Missing Skills"].split(","))
                if row["Missing Skills"] != "None"
                else 0
            )

            chart_df = pd.DataFrame(
                {
                    "Count": [
                        matched_count,
                        missing_count
                    ]
                },
                index=[
                    "Matched Skills",
                    "Missing Skills"
                ]
            )

            st.bar_chart(chart_df)            

            st.write(
                f"**Recommendation:** "
                f"{row['Recommendation']}"
            )

            if st.button(
                f"🤖 Generate AI Analysis - {row['Candidate']}",
                key=f"ai_{row['Candidate']}"
            ):

                try:

                    with st.spinner(
                        "Generating AI Analysis..."
                    ):

                        ai_summary = generate_ai_summary(
                            row["Resume Text"],
                            jd_text
                        )

                        st.markdown(ai_summary)

                except Exception as e:

                    st.error(
                        f"Gemini Error: {str(e)}"
                    )

