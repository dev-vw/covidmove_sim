#!/usr/bin/env python

"""
A script to load the required input data for the simulation
as pandas DataFrames

@author: vaniawang
"""

from pathlib import Path
import pandas as pd


def query_path():
    file_path = Path(input("Please enter the path of your RAW data: "))
    return file_path


def load_dat(dir_path):
    df_dict = {}
    for file_path in sorted(dir_path.rglob('*.csv')):
        print(file_path)
        df_dict[file_path.stem] = pd.read_csv(file_path)
    return df_dict


def gen_countyFIPs():
    print("PROCESSING COUNTY FIPS DATASET:")
    state_abbrv = str(input("Please enter the state abbreviation (ex: CA for California): "))
    file_path = Path(input("Please enter the path of your CBG data: "))
    fip_dat = pd.read_csv(file_path,
                          usecols=['state', 'countyFIPS'],
                          dtype={'state': 'object', 'countyFIPS': 'object'},
                          engine='python')
    fip_lst = list(fip_dat[fip_dat['state'] == state_abbrv].reset_index(drop=True).countyFIPS.unique())
    return fip_lst

def gen_countyPOP():
    print("PROCESSING COUNTY POPULATION DATASET:")
    state_abbrv = str(input("Please enter the state code (ex: 06 for California):"))
    file_path = Path(input("Please enter the path of your county population data: "))
    pop_dat = pd.read_csv(file_path,
                          usecols=['STATE', 'COUNTY', 'POPESTIMATE2019'],
                          dtype={'STATE': 'object',
                                 'COUNTY': 'object',
                                 'POPESTIMATE2019': 'int64'},
                          engine='python')

    # subsets the full dataset for the specified state only, while
    # also reindexing the dataframe
    pop_dat = pop_dat[pop_dat['STATE'] == '06'].reset_index(drop=True)

    # creates a new column, COUNTY_FIPS, that is the full FIP code of a county
    pop_dat['COUNTY_FIPS'] = pop_dat['STATE'] + pop_dat['COUNTY']

    return pop_dat

def process_dat(df_dict):
    pass

path = query_path()
df_dict = load_dat(path)
countyfip_lst = gen_countyFIPs()
countypop_dat = gen_countyPOP()
