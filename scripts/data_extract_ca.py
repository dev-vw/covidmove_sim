#!/usr/bin/env python

"""
This script does two things:
(1) subsets CA-only rows from csv files saved in the raw_dat/ directory 
(2) saves the CA extract in the dat/ directory

@author: vaniawang
"""

import pandas as pd
from pathlib import Path

dat_dir = Path("/home/vaniawang/Documents/proj/covidmove_sim/raw_dat/")

def get_california(path):
    """
    subsets csv for California rows ONLY
    """

    dat = pd.read_csv(path)
    dat = dat.loc[dat.state == 'California']

    return dat

def main():
    for path in sorted(dat_dir.rglob('*.csv')):
        dat = get_california(path)

        file_name = 'CAonly_' + path.name
        print(file_name)

        new_path = '/home/vaniawang/Documents/proj/covidmove_sim/dat/' + file_name
        dat.to_csv(path_or_buf=new_path, index=False)

if __name__ == "__main__":
    main()
