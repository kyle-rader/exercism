def hey(phrase: str):
    response = "Whatever."
    cleaned_phrase = phrase.replace(r"[\t\n]", " ").strip()
    is_question = cleaned_phrase.endswith("?")
    is_yelling = cleaned_phrase.isupper()

    if len(cleaned_phrase) == 0:
        response = "Fine. Be that way!"
    elif is_question and is_yelling:
        response = "Calm down, I know what I'm doing!"
    elif is_yelling:
        response = "Whoa, chill out!"
    elif is_question:
        response = "Sure."

    return response
