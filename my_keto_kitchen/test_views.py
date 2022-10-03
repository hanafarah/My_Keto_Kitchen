def test_index_ok(client):
    """make a GET request to / and store response object """
    response = client.get('/')
    assert response.status_code == 200
