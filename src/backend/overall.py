from completion import gpt3_completion

# generate prompt for summarising overall text
def meta_prompt(text):
    return f"Create a complete overall summary of the following extract from a video transcript.\n\nTranscript extract: \"\"\"\n{text}\n\"\"\"\n"


# invoke func for querying gpt-3 and summarise overall text
def meta_summarise(text):
    params = {
        "model":"text-davinci-003",
        "prompt":meta_prompt(text),
        "temp":0.6,
        "tokens":2000,
        "top_p":1,
        "freq_pen":0,
        "pres_pen":0
    }

    # summarise overall text with gpt3
    return gpt3_completion(**params)