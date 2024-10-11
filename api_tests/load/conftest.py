import pytest
import random

@pytest.fixture(scope="function")
def load_test_fixture():
    """Фикстура для нагрузочных API тестов."""
    return random.randint(100, 200)

@pytest.fixture(scope="module")
def api_common_fixture():
    """Переопределение общей API фикстуры для нагрузочных тестов."""
    return "API Load common (overridden)"
