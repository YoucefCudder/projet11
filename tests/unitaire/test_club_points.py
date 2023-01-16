

class TestEnoughPoints:

    def test_enough_points_to_purchase(self, client):
        response = client.post("/purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Fall Classic",
            "places": "1",
        })
        assert response.status_code == 200
        assert b'Success, booking complete!' in response.data

    def test_not_enough_points_to_purchase(self, client):
        response = client.post("/purchasePlaces", data={
            "club": "Iron Temple",
            "competition": "Fall Classic",
            "places": "11",
        })
        assert response.status_code == 200
        assert b'not enough points' in response.data
