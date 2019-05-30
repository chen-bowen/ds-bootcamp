import pytest

def test_get_metadata(client):
    res = client.get("/")
    assert res.status_code == 200

def test_get_metadata(client):
    res = client.get("/bye")
    assert res.status_code == 200