from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta
import string

# 11 char ID must then be parsed from video URL
# URL is used to fetch transcript summary and is segmented

def segment_transcript(vid_id):
    # SRT format is then obtained through YT transcript API
    try:
        srt = YouTubeTranscriptApi.get_transcript(vid_id)
    except: # transcript unavailable
        return "Unavailable" # return error 560

    # get length of video in seconds
    video_length = int(srt[-1]['start'] + srt[-1]['duration'])

    # check if video exceeds length limit of 100 mins
    if video_length > 6000: # 1hr40
        return "Max Length Exceeded" # return error 550

    # keep track of number of timestamps
    num_timestamps = len(srt)
    vid_segments = {}

    # iterate through srt list and separate timestamps in 5min interval
    interval = min(300, video_length)  # start in first 5min interval

    # create dict key containing timestamp string
    start, end = timedelta(seconds=0), timedelta(seconds=interval)
    timestamp = f"{start} - {end}"

    # add text segments to dictionary based in timestamp intervals
    for text_seg in srt:
        # remove newlines, space and rejoin sentences
        text = " ".join(text_seg['text'].split())

        # check punctuation to avoid mid sentence slicing
        if (text_seg['start'] < interval) or any([pct in text_seg['text'] for pct in string.punctuation]):
            if timestamp not in vid_segments:
                vid_segments[timestamp] = [text]
            else:
                vid_segments[timestamp].append(text)

        else:
            interval += 300  # move onto next interval
            start, end = timedelta(
                seconds=interval-300), timedelta(seconds=min(interval, video_length))
            timestamp = f"{start} - {end}"
            vid_segments[timestamp] = [text]  # don't lose current segment

    # join text for each timestamp segment
    for timestamp in vid_segments:
        vid_segments[timestamp] = " ".join(vid_segments[timestamp])

    # return dict with timestamped segments
    return vid_segments
