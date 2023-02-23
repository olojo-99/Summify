import pytest
import sys
# sys.path.insert(0, '../../backend')
from extraction import text_rank


# Checking number of key terms returned by spaCy TextRank component
def test_tr1():
    # example text
    text = "Most, but not all, genes have been identified by a combination of high throughput experimental and bioinformatics approaches."

    result = text_rank(text) # returns set of extracted terms

    assert len(result) >= 3

def test_tr2():
    # example text
    text = "Today, costs have fallen so far, that hard disk drives are being replaced with non-volatile, Solid State Drives, or SSDs."

    result = text_rank(text)

    assert len(result) >= 3

def test_tr3():
    # example text
    text = "Any data written to storage, like your hard drive, will stay there until it’s over-written or deleted, even if the power goes out."

    result = text_rank(text)

    assert len(result) >= 3