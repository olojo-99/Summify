from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta

# video URL will be received through GET request from quasar frontend
# 11 char ID must then be parsed from link
# URL is used to fetch transcript summary and is segmented


def segment_transcript(url):
    # "https://www.youtube.com/watch?v=rjYUeh3tlpc"

    vid_id = url  # chars 2-13 of 2nd list item

    # SRT format is then obtained through YT transcript API
    srt = YouTubeTranscriptApi.get_transcript(vid_id)

    # get length of video in seconds
    video_length = int(srt[-1]['start'] + srt[-1]['duration'])

    # keep track of number of timestamps
    num_timestamps = len(srt)

    # tokens = [segment['text'] for segment in srt]
    vid_segments = {}

    # iterate through srt list and separate timestamps in 5min interval
    interval = 300  # start in first 5min interval

    # create dict key containing timestamp string
    start, end = timedelta(seconds=interval-300), timedelta(seconds=interval)
    timestamp = f"{start} - {end}"

    # add text segments to dictionary based in timestamp intervals
    for text_seg in srt:
        # remove newlines, space and rejoin sentences
        text = " ".join(text_seg['text'].split())

        # include . to stop mid sentence slicing
        if text_seg['start'] < interval or "." in text_seg['text']:
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
