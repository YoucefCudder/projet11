from Python_Testing.server import load_competitions, load_clubs
from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):
    wait_time = between(2, 6)
    competitions = load_competitions()
    clubs = load_clubs()

    def on_start(self):
        self.client.post("showSummary", {"email": "john@simplylift.co"})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def get_board(self):
        self.client.get("/board")

    # @task
    # def booking(self):
    #     self.client.get("book/competitions['name']/clubs['name'])
