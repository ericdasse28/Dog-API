import os
from enum import Enum


class RequestType(Enum):
    """
    Enum class for RequestType contenant 4 valeurs - GET, POST, PUT, PATCH, DELETE

    """

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class DogAPI:
    def __init__(self):
        """
        Function to initialize the Dog API class
        """

        api_key = os.environ.get("API_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key,
        }
        self.base_url = "https://api.thedogapi.com/v1"
