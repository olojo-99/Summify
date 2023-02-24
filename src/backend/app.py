import os
from time import sleep
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_caching import Cache
from segment import segment_transcript
from rewrite import rewrite_segment
from summarise import sub_summarise
from overall import meta_summarise
from concurrency import thread_runner
from extraction import text_rank
from search import google_search
from utils import auto_transcript
from utils import err_handler


config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)  # creating instance of flask app with same name as file
CORS(app)  # activate cors

app.config.from_mapping(config)
cache = Cache(app) # only one cookie per client


# Return Timestamp/Segment pairs + Overall summary
@app.route("/summarise/<vid_id>", methods=["GET"])
@cache.cached(timeout=300) # caching summarisation results
def transcript_summary(vid_id):
    # Create dict of timestamps and matching transcript segment
    vid_segments = segment_transcript(vid_id)

    # return error if error found during transcription
    transcript_err = err_handler(vid_segments)
    if transcript_err:
        return transcript_err

    # Rewrite segments if auto-generated transcript
    if auto_transcript(vid_id):
        thread_runner(rewrite_segment, vid_segments) # multithreaded
        
        # return error if error found in gpt-3 rewriting completions
        gpt3_err =  err_handler(vid_segments)
        if gpt3_err:
            return gpt3_err

        sleep(1) # delay segment summarisation

    # Summarise segments of video transcript
    thread_runner(sub_summarise, vid_segments) # multithreaded

    # return error if error found in gpt-3 summarisation completions
    gpt3_err =  err_handler(vid_segments)
    if gpt3_err:
        return gpt3_err

    # Generate overall summary based on summarised segments
    all_segments = "\n".join(vid_segments.values())
    ovr_summary = meta_summarise(all_segments)

    # map video id to overall summary in cache
    all_summaries = f"{ovr_summary}\n{all_segments}"
    cache.set(vid_id, all_summaries)

    # Return GET response
    return jsonify(
        segments=vid_segments,
        overall=ovr_summary)


# Returns list of Google links
@app.route("/links/<vid_id>", methods=["GET"])
@cache.cached(timeout=300) # caching IR results
def ir_links(vid_id):
    # get cached summary for video
    summaries = cache.get(vid_id)

    # run summaries through textrank algorithm
    terms = list(text_rank(summaries))

    # perform search on terms
    search_results = google_search(terms)

    # error check for search results
    search_err = err_handler(search_results)
    if search_err:
        return search_err

    # Return GET response
    return jsonify(search_results)


# Run application
if __name__ == '__main__':
    app.run()
