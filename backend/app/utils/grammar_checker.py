import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    matches = tool.check(text)

    issues = []
    for m in matches:
        # 🔥 Skip very short errors (like single letters, symbols)
        if len(m.context.strip()) < 3:
            continue

        issues.append(m.message)

    return issues