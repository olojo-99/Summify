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
from video_info import auto_transcript
from parallel import thread_runner
from extraction import topic_rank
from search import google_search

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)  # creating instance of flask app with same name as file
CORS(app)  # activate cors

app.config.from_mapping(config)
cache = Cache(app) # only one cookie per client

# GET request from Frontend will contain video id in request vid_id
# Full video URL needs to be parsed on frontend

# Return Timestamp/Segment pairs + Overall summary
@app.route("/summarise/<vid_id>", methods=["GET"])
@cache.cached(timeout=300) # caching summarisation results
def transcript_summary(vid_id):
    # vid_id = "Unl1jXFnzgo"  # EXAMPLE MANUAL TRANSCRIPT ID

    # Create dict of timestamps and matching transcript segment
    vid_segments = segment_transcript(vid_id)
    # return error if empty dict (max length exceeded)
    if vid_segments == "Max Length Exceeded":
        return "Video exceeds maximum length", 550
    elif vid_segments == "Unavailable":
        return "Transcript Unavailable", 560

    # Rewrite segments if auto-generated transcript
    if auto_transcript(vid_id):
        thread_runner(rewrite_segment, vid_segments) # parallelised
        # vid_segments = {stamp: rewrite_segment(vid_segments[stamp]) for stamp in vid_segments}
        sleep(1) # delay segment summarisation

    # Summarise segments of video transcript
    thread_runner(sub_summarise, vid_segments) # parallelised
    # vid_segments = {stamp: sub_summarise(vid_segments[stamp]) for stamp in vid_segments}

    # Generate overall summary based on summarised segments
    all_segments = "\n".join(vid_segments.values())
    ovr_summary = meta_summarise(all_segments)

    # map video id to overall summary in cache
    all_summaries = f"{ovr_summary}\n{all_segments}"
    cache.set(vid_id, all_summaries)

    return jsonify(
        segments=vid_segments,
        overall=ovr_summary)


# GET request from Frontend for Google links will have no body
# Links will be based on Fact Extraction on summarised segments

# Returns list of Google links
@app.route("/links/<vid_id>", methods=["GET"])
@cache.cached(timeout=300) # caching IR results
def ir_links(vid_id):
    # get cached overall summary for video
    summaries = cache.get(vid_id)

    # run summaries through topicrank algorithm
    terms = list(topic_rank(summaries))

    # perform search on terms
    search_results = google_search(terms)

    return jsonify(search_results)

# !L!0!U!I!$!€!

# Run application
if __name__ == '__main__':
    app.run()
