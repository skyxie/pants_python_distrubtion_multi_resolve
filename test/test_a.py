import pandas as pd

from a import group_value_counts


def test_group_value_counts():
    orig = pd.DataFrame(
        [("foo", 1), ("foo", 2), ("bar", 1)], columns=("lorem", "ipsum")
    )
    act = group_value_counts(orig)
    exp = pd.DataFrame(
        {
            "column": [
                "~~ ipsum ~~",
                "~~ ipsum ~~",
                "~~ lorem ~~",
                "~~ lorem ~~",
            ],
            "label": [1, 2, "bar", "foo"],
            "count": [2, 1, 1, 2],
        }
    )
    pd.testing.assert_frame_equal(act, exp, check_index_type=False, check_like=True)
