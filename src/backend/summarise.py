from completion import gpt3_completion
from utils import completion_err

# generate prompt for summarising segments
def sub_prompt(extract):
    return f"The following is an extract from a video transcript. Rewrite this as a structured, clear summary.\n\nVideo Transcript Extract: \"\"\"\n{extract}\n\"\"\"\n"


# invoke func for querying gpt-3 and summarise transcript segment
def sub_summarise(segment):
    params = {
        "model": "text-curie-001",
        "prompt": sub_prompt(segment),
        "temp": 0.6,
        "tokens": 300,
        "top_p": 1,
        "freq_pen": 0,
        "pres_pen": 0
    }

    # summarise segment with gpt3
    return completion_err( gpt3_completion(**params) )
