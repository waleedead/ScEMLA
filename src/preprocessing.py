import pandas as pd

def preprocess_data(df):
    df_filtered = df.loc[(df.sum(axis=1) > 200) & (df.sum(axis=1) < 2500)]
    return df_filtered
