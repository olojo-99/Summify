import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3_completion(model, prompt, temp, top_p, tokens, freq_pen, pres_pen):
    # try:
    print(prompt)
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen
    )
    print(response)

    # return gpt3 text response
    # need to remove unnecessary chars from response
    return (response.choices[0].text.strip("\n"))

    # except:
    #     return "Error generating GPT-3 Completion\n"
