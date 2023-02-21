import os
from dotenv import load_dotenv
import openai
import time

load_dotenv() # take environment variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3_completion(model, prompt, temp, top_p, tokens, freq_pen, pres_pen):
    # make up to 3 GPT-3 calls
    max_retry , retry = 3, 0
    while True:
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen
            )

            # return gpt3 text response
            return (response.choices[0].text.strip("\n"))

        except Exception as error:
            # make another attempt at the API call
            retry += 1
            # check number of attempts
            if retry < max_retry:
                sleep(2)
                continue # return to start of call
            else:
                return "Error generating GPT-3 Completion\n"
