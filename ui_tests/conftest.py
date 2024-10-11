import pytest

@pytest.fixture(scope="module")
def ui_common_fixture():
    """Фикстура для всех UI тестов."""
    return "UI common"
