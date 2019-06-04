import pytest
from hypothesis import strategies as st, given, reproduce_failure
from ds_bootcamp.flask_app import MAX_VALUE, MIN_VALUE

def test_get_metadata(client):
    res = client.get("/bowen_hello")
    assert res.status_code == 200

def test_get_metadata2(client):
    res = client.get("/bowen_bye")
    assert res.status_code == 200

def test_get_simple_model(client):
    res = client.get("/simple_model/submodel_1/10")
    assert  res.status_code == 200
    assert res.json['score'] == 25

def test_no_model(client):
    res = client.get("/simple_model/submodel_3/10")
    assert res.status_code == 404

@given(x=st.integers(min_value=MIN_VALUE, max_value=MAX_VALUE))
def test_simple_model_hypothesis(client, x):
    res =  client.get(f"/simple_model/submodel_1/{x}")
    assert res.status_code == 200
    assert res.json['score'] == 5 + 2*x

@given(x=st.integers(min_value=MAX_VALUE + 1))
def test_simple_model_high_value(client, x):
    res =  client.get(f"/simple_model/submodel_1/{x}")
    assert res.status_code == 400

@given(x=st.integers(max_value=MIN_VALUE - 1))
def test_simple_model_low_value(client, x):
    res =  client.get(f"/simple_model/submodel_1/{x}")
    assert res.status_code == 400