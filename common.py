#!/usr/bin/env python3
import pandas as pd

REGION_MAP = {'af-south-1':'Cape Town', 'ap-south-1':'Mumbai', 'ap-southeast-1':'Singapore', 'ap-southeast-2':'Sydney',
                  'ap-northeast-1':'Tokyo', 'eu-west-2':'London', 'me-south-1':'Bahrain', 'sa-east-1':'Sao Paulo', 
              'us-west-1':'N. California'}

REGION_ORDER = ['N. California', 'Tokyo', 'London', 'Sydney', 'Singapore',
            'Sao Paulo', 'Bahrain', 'Mumbai', 'Cape Town']

plot_params = {
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9, 
    "ytick.labelsize": 8, 
    "xtick.labelsize": 8, 
    'legend.fontsize': 8, 
    'legend.title_fontsize': 9
}
sns_params = {
    'figure.figsize': (7.16, 3),
    'figure.dpi': 300,
    "font.size": 9,
    'figure.titlesize': 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9, 
    "ytick.labelsize": 8, 
    "xtick.labelsize": 8, 
    'legend.fontsize': 8, 
    'legend.title_fontsize': 9
}

region_mapping = dict(Africa_Cape_Town='Cape Town', Asia_Pacific_Mumbai='Mumbai', Asia_Pacific_Singapore='Singapore',
                     Asia_Pacific_Sydney='Sydney', Asia_Pacific_Tokyo='Tokyo', Europe_London='London',
                     Middle_East_Bahrain='Bahrain', South_America_Sao_Paulo='Sao Paulo', US_West_N_California='N. California')

def combine_csvs(src, ind_col=0, header='infer'):
    dfs = [pd.read_csv(f, index_col=ind_col, header=header) for f in src]
    return pd.concat([df for df in dfs if not df.empty])