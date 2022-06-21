#!/usr/bin/env python3
import pandas as pd

region_mapping = dict(Africa_Cape_Town='Cape Town', Asia_Pacific_Mumbai='Mumbai', Asia_Pacific_Singapore='Singapore',
                     Asia_Pacific_Sydney='Sydney', Asia_Pacific_Tokyo='Tokyo', Europe_London='London',
                     Middle_East_Bahrain='Bahrain', South_America_Sao_Paulo='Sao Paulo', US_West_N_California='N. California')

def combine_csvs(src, ind_col=0, header='infer'):
    return pd.concat([pd.read_csv(f, index_col=ind_col, header=header) for f in src])