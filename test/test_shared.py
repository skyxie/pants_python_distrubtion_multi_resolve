from shared import fancy_string


def test_fancy_string():
    assert fancy_string("foo") == "~~ foo ~~"
