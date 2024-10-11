import pytest
import random

@pytest.fixture(scope="session")
def common_fixture():
    """Фикстура для всех тестов проекта."""
    return random.randint(1, 100)
