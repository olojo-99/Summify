import pytest
import sys
# sys.path.insert(0, '../../backend')
from search import google_search


# Checking number of links returned by API to custom google search engine
def test_gs1():
    # example terms
    terms = ["Genes", "high throughput experimental", "bioinformatics approaches"]

    result = google_search(terms) # returns set of wiki links

    assert len(result) == len(terms)

def test_gs2():
    # example terms with 2 similarities
    terms = ["Quantum Computing", "Quantum Entanglement", "Quantum Computer"]

    result = google_search(terms)

    assert len(result) == len(terms) - 1 # 2 distinct wiki pages
