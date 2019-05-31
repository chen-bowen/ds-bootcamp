import pytest

def test_get_metadata(client):
    res = client.get("/bowen_hello")
    assert res.status_code == 200

def test_get_metadata2(client):
    res = client.get("/bowen_bye")
    assert res.status_code == 200

def test_get_simple_model(client):
    res = client.get("/simple_model/submodel_1/10")
    assert  res.status_code == 200
    assert res.json['score'] == 10

def test_no_model(client):
    res = client.get("/simple_model/submodel_3/10")
    assert res.status_code == 404