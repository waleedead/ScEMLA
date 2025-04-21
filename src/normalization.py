import numpy as np

def normalize_data(df):
    df_log = np.log1p(df)
    return (df_log - df_log.mean()) / df_log.std()
