import language_tool_python
import re

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):

    matches = tool.check(text)

    errors = []

    for match in matches:
        error_text = text[match.offset: match.offset + match.error_length]

        # 🔴 IGNORE CASES

        # 1. Proper nouns (capitalized words like names)
        if error_text.istitle():
            continue

        # 2. Emails
        if re.match(r"\S+@\S+\.\S+", error_text):
            continue

        # 3. URLs
        if re.match(r"http[s]?://", error_text):
            continue

        # 4. Tech words (basic filter)
        if any(char.isdigit() for char in error_text):
            continue

        # 5. Very short words (often noise)
        if len(error_text) <= 2:
            continue

        errors.append({
            "message": match.message,
            "suggestions": match.replacements[:3],
            "error_text": error_text
        })

    return {
        "total_errors": len(errors),
        "top_errors": errors[:10]
    }