from youtube_transcript_api import YouTubeTranscriptApi

# Determine whether transcript is written manually or auto-generated
def auto_transcript(vid_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(vid_id)
    transcript = transcript_list.find_transcript(['en'])

    # make api call for each segment -> need to parallelise
    if transcript.is_generated:
        return True
    else:
        return False

# Error handling for /summarise responses
def err_handler(response):
    # Returns error message, error code
    if response == "Max Length Exceeded":
        return "Video exceeds maximum length", 550

    elif response == "Unavailable":
        return "Transcript Unavailable", 560

    elif "GPT-3 Error" in response:
        return "Error Generating GPT-3 Completion", 570

    elif response == "Custom Search Engine Error":
        return "Custom Search Engine Unavailable", 580

    else:
        return None # No errors found


# Error checking for when GPT-3 is unavailable
def completion_err(response):
    if response == "Error generating GPT-3 Completion":
        return "GPT-3 Error"

    else:
        return response
