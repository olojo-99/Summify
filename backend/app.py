import os
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS
from segment import segment_transcript
from rewrite import rewrite_segment
from summarise import sub_summarise
from overall import meta_summarise
from video_info import manual_transcript
from parallel import thread_runner


# OpenAI API key hidden in environment variable file

app = Flask(__name__)  # creating instance of flask app with same name as file
CORS(app)  # activate cors


# GET request from Frontend will contain video id in request vid_id
# Full video URL needs to be parsed on frontend

# Return Timestamp/Segment pairs + Overall summary
@app.route("/summarise/<vid_id>", methods=["GET"])
def transcript_summary(vid_id):

    # vid_id = "Unl1jXFnzgo"  # EXAMPLE MANUAL TRANSCRIPT ID

    # Create dict of timestamps and matching transcript segment
    vid_segments = segment_transcript(vid_id)

    # Rewrite segments if auto-generated transcript
    if manual_transcript(vid_id):
        # vid_segments = {stamp: rewrite_segment(vid_segments[stamp]) for stamp in vid_segments}
        thread_runner(rewrite_segment, vid_segments)

    # Summarise segments of video transcript
    # vid_segments = {stamp: sub_summarise(vid_segments[stamp]) for stamp in vid_segments}
    thread_runner(sub_summarise, vid_segments)

    # Generate overall summary based on summarised segments
    ovr_summary = meta_summarise("\n".join(vid_segments.values()))

    return jsonify(
        segments=vid_segments,
        overall=ovr_summary)


# GET request from Frontend for Google links will have no data
# Links will be based on Fact Extraction on summarised segments

# Returns list of Google links
@app.route("/links", methods=["GET"])
def ir_links():
    return "Information Retrieval Links"


# Run application
if __name__ == '__main__':

    app.run()
