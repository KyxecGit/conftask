def test_functional_api(api_common_fixture, common_fixture):
    assert api_common_fixture == "API common"
    assert isinstance(common_fixture, int)
