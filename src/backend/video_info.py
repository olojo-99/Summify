from youtube_transcript_api import YouTubeTranscriptApi

def auto_transcript(vid_id):

    # Determine whether transcript is written manually or auto-generated
    transcript_list = YouTubeTranscriptApi.list_transcripts(vid_id)
    transcript = transcript_list.find_transcript(['en'])

    # make api call for each segment -> need to parallelise
    if transcript.is_generated:
        return True
    else:
        return False


# def invalid_length(vid_id, vid_length):
#     # return true for auto or manual vids that exceed length limit
#     if auto_transcript(vid_id):
#         if vid_length > 3600: # 1h
#             return True
#     else: # manual transcript
#         if vid_length > 5400: # 1h30
#             return True

#     return False # valid length
