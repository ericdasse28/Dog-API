from enum import Enum


class RequestType(Enum):
    """
    Enum class for RequestType contenant 4 valeurs - GET, POST, PUT, PATCH, DELETE

    """

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"
