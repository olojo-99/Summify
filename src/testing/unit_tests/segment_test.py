import pytest
import sys
# sys.path.insert(0, '../../backend')
from segment import segment_transcript


# Provide URL for YT video and test segment lengths
def test_segment1():
    vid_id = "JBjjnqG0BP8" # 4m 47s
    segments = segment_transcript(vid_id)

    assert len(segments) == 1

def test_segment2():
    vid_id = "tc4ROCJYbm0" # 27m 26s
    segments = segment_transcript(vid_id)

    assert len(segments) == 6

def test_segment3():
    vid_id = "Sg4U4r_AgJU" # 60m 05s
    segments = segment_transcript(vid_id)

    assert len(segments) == 12

def test_segment4():
    vid_id = "lY54TmmEllY" # 66m 28s
    segments = segment_transcript(vid_id)

    assert len(segments) == 14