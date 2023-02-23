import pytest
import json
from flask import Flask
import sys
sys.path.insert(0, '../../backend')
import requests


def test_summarise1():
    # Video ID
    endpoint = 'http://127.0.0.1:5000/summarise/Unl1jXFnzgo'

    req = requests.get(endpoint)
    data = req.json()

    # check status code and minimum overall + segment summary response
    assert req.status_code == 200 and len(data) >= 2


def test_summarise2():
    endpoint = 'http://127.0.0.1:5000/summarise/TQCr9RV7twk'

    req = requests.get(endpoint)
    data = req.json()

    assert req.status_code == 200 and len(data) >= 2


def test_summarise3():
    # Transcript unavailable
    endpoint = 'http://127.0.0.1:5000/summarise/ZcpwnozMh2U'

    req = requests.get(endpoint)

    # check correct error code
    assert req.status_code == 560


def test_summarise4():
    # Exceeds maximum length
    endpoint = 'http://127.0.0.1:5000/summarise/NWONeJKn6kc'

    req = requests.get(endpoint)

    # check correct error code
    assert req.status_code == 550


def test_ir1():
    endpoint = 'http://127.0.0.1:5000/links/Unl1jXFnzgo'

    req = requests.get(endpoint)
    data = req.json()

    # check status code and minimum 3 wiki links response
    assert req.status_code == 200 and len(data) >= 3


def test_ir2():
    endpoint = 'http://127.0.0.1:5000/links/TQCr9RV7twk'

    req = requests.get(endpoint)
    data = req.json()

    # check status code and minimum 3 wiki links response
    assert req.status_code == 200 and len(data) >= 3

