# coding=utf-8


def test_api_hello(client):
    response = client.get("/apis/hello")
    assert response.data == b"Hello Api"
