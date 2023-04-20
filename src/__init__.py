import pandas as pd

from shared import fancy_string


def group_value_counts(df: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    for col in df.columns:
        col_val_counts = df[col].value_counts()
        col_df = col_val_counts.reset_index()
        col_df.columns = ("label", "count")
        col_df.loc[:, "column"] = fancy_string(col_val_counts.name)
        dfs.append(col_df)
    return pd.concat(dfs).sort_values(by=("column", "label"))