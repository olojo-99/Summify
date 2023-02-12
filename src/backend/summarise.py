from completion import gpt3_completion

# generate prompt for summarising segments


def sub_prompt(extract):
    # return f"Summarise the following video segment.\n\nvideo segment: \"\"\"\n{extract}\n\"\"\"\n"
    return f"The following is an extract from a video transcript. Rewrite this as a structured, clear summary. Focus on important facts while keeping the overall structure of the text.\n\nVideo Transcript Extract: \"\"\"\n{extract}\n\"\"\"\n"
    # return f"Summarise the following extract from a video transcript, focusing on important facts while still keeping the overall structure of the text.\n\nTranscript: \"\"\"\n{extract}\n\"\"\"\n"


# invoke func for querying gpt-3 and summarise transcript segment
def sub_summarise(segment):
    params = {
        # "model": "text-davinci-003",
        "model": "text-curie-001",
        "prompt": sub_prompt(segment),
        "temp": 0.6,
        "tokens": 500,
        "top_p": 1,
        "freq_pen": 0,
        "pres_pen": 0
    }

    # summarise segment with gpt3
    return gpt3_completion(**params)
