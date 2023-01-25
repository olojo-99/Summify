from completion import gpt3_completion

# generate prompt for rewriting auto generated transcipts
def rewrite_prompt(extract):
    return f"The following is an unstructured video transcript. Please rewrite this as a more structured, clear essay.\n\nTranscript: \"\"\"\n{extract}\n\"\"\"\n"


# invoke func for querying gpt-3 and rewrite transcript segment
def rewrite_segment(segment):
    params = {
        "model":"text-davinci-003",
        "prompt":rewrite_prompt(segment),
        "temp":0.6,
        "tokens":1000,
        "top_p":1,
        "freq_pen":0,
        "pres_pen":0
    }

    # rewrite segment with gpt3
    return gpt3_completion(**params)