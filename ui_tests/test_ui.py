def test_ui_example(ui_common_fixture, common_fixture):
    assert ui_common_fixture == "UI common"
    assert isinstance(common_fixture, int)
