import os
import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__) # creating instance of flask app with same name as file

# # create and add a new api key from https://beta.openai.com/account/api-keys
# openai.api_key = "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"

# # add route decorator for index func, which specifies what is returned at index route
# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         extract = request.form["transcript"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(extract),
#             temperature=0.6,
#             max_tokens=1000,
#         )
#         # redirect the user to the URL for the index page (/) with URL result parameter passed
#         # may want to find method for hiding result param within URL
#         return redirect(url_for("index", result=response.choices[0].text))


#     summary = request.args.get("result") # obtain summary result from URL param dict
#     print(f'\n\n{summary}\n\n') # print to CLI for debugging
#     return render_template("index.html", result=summary) # render HTML page with result in div


# # prompt is specified in docstring and passed to model
# def generate_prompt(extract):
#     return f"Create a summary of the following extract from a video transcript:\n\n{extract}"



@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run()