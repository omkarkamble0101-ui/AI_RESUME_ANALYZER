def generate_suggestions(matched_skills, missing_skills):

        suggestions = []

        skill_map = {
            "python": "Build backend projects using FastAPI or Django",
            "java": "Develop OOP-based applicatoins or Spring Boot projects",
            "c++": "Practice dta structures and comeptitive programming",
            "sql": "Practice joins, indexing and query ootimization",
            "mongodb": "Build NoSQL projects and understand aggregation pipeline",

            "html": "Create sturctured web pages with semantic tags",
            "css": "Design responsive layouts using Flexbox/Grid",
            "javascript": "Build dynamic UI and learn ES6 concepts",
            "react": "Build frontend apps using components and hooks",

            "node": "Develop backend services using Node.js",
            "express": "Create REST APIs using Express framework",
            "fastapi": "Build high-performance APIs using FastAPI",

            "machine learning": "Work on read datasets using sklearn and build models",
            "data analysis": "Analyze datasets using pandas and visualization tools",

            "aws": "Learn AWS basics like EC2, S3 and deploy a project",
            "docker": "Containerize your applications using Docker",
            "react": "Build frontend apps using React and hooks"
        }

        for skill in missing_skills[:5]:
            if skill in skill_map:
                suggestions.append(f"Learn {skill}: {skill_map[skill]}")
            else:
                suggestions.append(f"Gain practical experience in {skill}")

        for skill in matched_skills[:3]:

            suggestions.append(f"Srengthen {skill} with real-world projects")

        general_tips = [
            "Use action verbs like 'developed', 'implemented', 'designed'",
            "Add measurable achievements (e.g., improved performance by 20%)",
            "Keep resume concise and relevant",
            "Highlight projects and practical experience"
        ]

        return {
            "skill_suggestions": suggestions,
            "general_tips": general_tips
        }