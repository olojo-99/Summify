from youtube_transcript_api import YouTubeTranscriptApi


def manual_transcript(vid_id):

    # Determine whether transcript is written manually or auto-generated
    transcript_list = YouTubeTranscriptApi.list_transcripts(vid_id)
    transcript = transcript_list.find_transcript(['en'])

    # make api call for each segment -> need to parallelise
    if transcript.is_generated:
        return True
    else:
        return False
