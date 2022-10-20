from Python_Testing import server


def test_update(client):
    # points_before = server.clubs[1]['points']
    response = client.post('/purchasePlaces', data={
        "club": "Simply Lift",
        "competition": 'Fall Classic',
        "places": 3
    })

    update = client.get('/boards')
    assert b'Success, booking complete!' in response.data
    assert response.status_code == 200
    assert server.competitions[1]['numberOfPlaces'] == 10 in response.data
    assert server.clubs[1]['points'] == f'4' in update.data.decode()


def test_login_and_logout(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome, john@simplylift.co" in data

    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data
