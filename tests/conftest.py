import pytest

from Python_Testing.server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client