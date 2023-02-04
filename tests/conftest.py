import pytest

from dog_api.core import DogAPI


@pytest.fixture
def dog_api():
    return DogAPI()
