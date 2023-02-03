import json
import logging
import os
from enum import Enum

import requests

logging.basicConfig(level=logging.INFO)


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

    def call_api(self, request_type: str, endpoint: str, payload: dict | str = None):
        """Function to call the API via the Requests Library

        Args:
            request_type (str): Type of Request
            endpoint (str): API Endpoint
            payload (dict | str, optional): API Request Parameters or Query String. Defaults to None.
        Returns:
            Response (list | dict): JSON formatted response
        """

        try:
            response = ""

            if request_type == "GET":
                response = requests.get(
                    endpoint,
                    timeout=30,
                    payload=payload,
                )
            elif request_type == "POST":
                response = requests.post(
                    endpoint,
                    headers=self.headers,
                    timeout=30,
                    json=payload,
                )

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                return json.dumps(
                    {"ERROR": "Authorization Error. Please check API key"}
                )

            response.raise_for_status()

        except requests.exceptions.HTTPError as errh:
            logging.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.error(errc)
        except requests.exceptions.Timeout as errt:
            logging.error(errt)
        except requests.exceptions.RequestException as err:
            logging.error(err)

    def list_breeds(self, query_dict: dict) -> list:
        """Function to list dog breeds

        Args:
            query_dict (dict): Query string parameters

        Returns:
            list: JSON formatted list of all dog breeds on the API
        """

        if not isinstance(query_dict, dict):
            raise ValueError("ERROR - Parameter 'query_dict' should be of type dict")

        breeds_url = f"{self.base_url}/breeds"

        response = self.call_api(
            request_type=RequestType.GET.value,
            endpoint=breeds_url,
            payload=query_dict,
        )

        return response

    def search_breeds(self, query_str: str) -> list:
        """Function to search dog breeds

        Args:
            query_str (str): Dog breed we are looking for

        Returns:
            list: JSON formatted response
        """

        if not isinstance(query_str, str):
            raise ValueError("ERROR - Parameter 'query_str' should be of type string")

        search_breeds_url = f"{self.base_url}/breeds/search"

        response = self.call_api(
            request_type=RequestType.GET.value,
            endpoint=search_breeds_url,
            payload={"q": query_str},
        )

        return response
