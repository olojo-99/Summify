import os
import openai

#openai.api_key = "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"

def gpt3_completion(model, prompt, temp, top_p, tokens, freq_pen, pres_pen):
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
        return (response.choices[0].text.strip("\n")) # need to remove unnecessary chars from response

    except:
        return "Error generating GPT-3 Completion\n"
