from completion import gpt3_completion
from utils import completion_err

# generate prompt for summarising overall text
def meta_prompt(text):
    return f"The following is a combination of video extract summaries. Rewrite this as a structured, clear summary.\n\nCombined Transcript Extracts: \"\"\"\n{text}\n\"\"\"\n"


# invoke func for querying gpt-3 and summarise overall text
def meta_summarise(text):
    params = {
        "model": "text-davinci-003",
        "prompt": meta_prompt(text),
        "temp": 0.6,
        "tokens": 300,
        "top_p": 1,
        "freq_pen": 0,
        "pres_pen": 0
    }

    # summarise overall text with gpt3
    return completion_err( gpt3_completion(**params) )
