from locust import HttpUser
from locust import task

class HelloUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/")