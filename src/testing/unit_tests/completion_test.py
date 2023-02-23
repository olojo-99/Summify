import pytest
import sys
# adding backend to the system path
sys.path.insert(0, '../../backend')
from rewrite import rewrite_segment
from summarise import sub_summarise
from overall import meta_summarise


# Checking response for rewriting with GPT-3
def test_rewrite():
    # example video segment
    segments = {300: "Most, but not all, genes have been identified by a combination of high throughput experimental and bioinformatics approaches."}

    response = rewrite_segment(segments)

    assert len(response) > 1

# Checking response for segment summary with GPT-3
def test_sub():
    segments = {600: "There is no consensus on what constitutes a functional element in the genome since geneticists, evolutionary biologists, and molecular biologists employ different definitions and methods."}

    response = sub_summarise(segments)

    assert len(response) > 1

# Checking single response for overall summary of multiple segments with GPT-3
def test_ovr():
    segments = {300: "Tag players, as a quadrant, are going to be the biggest winners.",
                600: "Lag players, someone who's very aggressive and plays a lot of hands, could possibly be a pretty good winner." }

    response = [(meta_summarise(segments))] # enter single string into list

    assert len(response) == 1 # check for single overall summary