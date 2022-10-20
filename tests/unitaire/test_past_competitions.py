

class TestBookingPastCompetition:

    def test_book_present_competition(self, client):
        response = client.post("/purchasePlaces", data={
            "club": "She Lifts",
            "competition": "Fall Classic",
            "places": "2",
        })
        assert response.status_code == 200
        assert b'Success, booking complete!' in response.data

    def test_book_past_competition(self, client):
        response = client.post("/purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Spring Festival",
            "places": "2",
        })
        assert response.status_code == 200
        assert b'Competition already passed, choose a competition still open' in response.data

