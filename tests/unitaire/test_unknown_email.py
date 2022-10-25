from Python_Testing import server


class TestUnknownEmail:

    def test_conform_email(self, client):
        landing = client.post('/showSummary', data={'email': server.clubs[2]['email']})
        result_decoded = landing.data.decode()
        assert landing.status_code == 200

    def test_wrong_email(self, client):
        landing = client.post('/showSummary', data={'email': 'you.aouali@gmail.com'})
        assert landing.status_code == 200

    def test_empty_email(self, client):
        landing = client.post('/showSummary', data={'email': ""})
        assert landing.status_code == 200
