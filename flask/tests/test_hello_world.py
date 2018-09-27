# coding=utf-8


def test_hello_world(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
