from Python_Testing.server import competitions, clubs


class TestForTwelvePoints:
    def test_cant_book_more_than_twelve_places(self, client):
        response = client.post("/purchasePlaces", data={"places": 14,
                                                        "club": clubs[0]["name"],
                                                        "competition": competitions[1]["name"]
                                                        })
        assert response.status_code == 200
        assert "12 places maximum please" in response.data.decode()

    def test_can_book_less_than_twelve_places(self, client):
        response = client.post("/purchasePlaces", data={"places": 1,
                                                        "club": clubs[1]["name"],
                                                        "competition": competitions[1]["name"]
                                                        })
        assert response.status_code == 200
        assert "Success, booking complete!" in response.data.decode()
