import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope='function', autouse=True)
def driver(request: FixtureRequest):
    request.cls.driver = None