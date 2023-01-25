from completion import gpt3_completion

# generate prompt for summarising segments
def sub_prompt(extract):
    return f"Summarise the following extract from a video transcript.\n\nTranscript: \"\"\"\n{extract}\n\"\"\"\n"


# invoke func for querying gpt-3 and summarise transcript segment
def sub_summarise(segment):
    params = {
        "model":"text-davinci-003",
        "prompt":sub_prompt(segment),
        "temp":0.6,
        "tokens":1000,
        "top_p":1,
        "freq_pen":0,
        "pres_pen":0
    }

    # summarise segment with gpt3
    return gpt3_completion(**params)