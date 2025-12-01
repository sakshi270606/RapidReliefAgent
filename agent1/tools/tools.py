def summarizer(text):
    return text[:100] + "..." if len(text) > 100 else text
