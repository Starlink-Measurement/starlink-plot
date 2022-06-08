#!/usr/bin/env python3
import pandas as pd

def combine_csvs(src, ind_col=0):
    return pd.concat([pd.read_csv(f, index_col=ind_col) for f in src])