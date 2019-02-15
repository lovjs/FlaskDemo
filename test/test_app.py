# http://flask.pocoo.org/docs/1.0/testing/

import os
import pytest

from app.main import app

# This will get called before every test and can be used to set up a testing DB
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_title(client):
    """Verify the title"""
    rv = client.get('/')
    assert b'Multiplication table' in rv.data

def test_multiplication_POST(client):
    """Verify multiplication works"""
    rv = client.post('/', data={'a':5, 'b':6}) # sends a and b as post values
    assert b'1' in rv.data


def test_multiplication_GET(client):
    """Verify multiplication works"""
    rv = client.get('/?a=5&b=10') 
    assert b'50' in rv.data

    rv = client.get('/?a=9&b=9')
    assert b'81' in rv.data
