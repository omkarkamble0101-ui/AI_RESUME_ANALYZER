from app.utils.skills import SKILLS

def analyze_resume(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    score = int((len(found_skills) / len(SKILLS)) * 100)

    missing_skills = list(set(SKILLS) - set(found_skills))

    return {
        "skills_found": found_skills,
        "missing_skills": missing_skills,
        "score": score
}