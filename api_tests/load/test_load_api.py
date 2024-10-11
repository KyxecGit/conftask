def test_load_api(api_common_fixture, load_test_fixture, common_fixture):
    assert api_common_fixture == "API Load common (overridden)"
    assert isinstance(load_test_fixture, int)
    assert isinstance(common_fixture, int)
