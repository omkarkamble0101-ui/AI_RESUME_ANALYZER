def match_resume_with_job(resume_text, job_description):
    from app.utils.skill_extractor import extract_skills

    # Extract skills instead of raw words
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    resume_skills_set = set(resume_skills)
    job_skills_set = set(job_skills)

    matched = list(resume_skills_set & job_skills_set)
    missing = list(job_skills_set - resume_skills_set)

    if len(job_skills_set) == 0:
        match_score = 0
    else:
        match_score = int((len(matched) / len(job_skills_set)) * 100)

    return {
        "match_score": match_score,
        "matched_skills": matched,
        "missing_skills": missing
    }