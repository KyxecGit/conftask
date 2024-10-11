import pytest

@pytest.fixture(scope="module")
def api_common_fixture():
    """Фикстура для всех API тестов."""
    return "API common"
