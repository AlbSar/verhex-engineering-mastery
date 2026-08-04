from week001.environment import runtime_name


def test_runtime_name_returns_python() -> None:
    assert runtime_name() == "Python"
