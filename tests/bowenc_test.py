import pytest

def test_get_metadata(client):
    res = client.get("/bowen_hello")
    assert res.status_code == 200

def test_get_metadata(client):
    res = client.get("/bowen_bye")
    assert res.status_code == 200