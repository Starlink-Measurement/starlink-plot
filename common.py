#!/usr/bin/env python3
import pandas as pd

REGION_MAP = {'af-south-1':'Africa Cape Town', 'ap-south-1':'Asia Pacific Mumbai', 'ap-southeast-1':'Asia Pacific Singapore', 'ap-southeast-2':'Asia Pacific Sydney',
                  'ap-northeast-1':'Asia Pacific Tokyo', 'eu-west-2':'Europe London', 'me-south-1':'Middle East Bahrain', 'sa-east-1':'South America Sao Paulo', 
              'us-west-1':'US West N. California'}

plot_params = {
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
}
sns_params = {"font.size":9,"axes.titlesize":9,"axes.labelsize":8, "xtick.labelsize":8, 'legend.fontsize': 8, 'legend.title_fontsize': 9}

region_mapping = dict(Africa_Cape_Town='Cape Town', Asia_Pacific_Mumbai='Mumbai', Asia_Pacific_Singapore='Singapore',
                     Asia_Pacific_Sydney='Sydney', Asia_Pacific_Tokyo='Tokyo', Europe_London='London',
                     Middle_East_Bahrain='Bahrain', South_America_Sao_Paulo='Sao Paulo', US_West_N_California='N. California')

def combine_csvs(src, ind_col=0, header='infer'):
    return pd.concat([pd.read_csv(f, index_col=ind_col, header=header) for f in src])