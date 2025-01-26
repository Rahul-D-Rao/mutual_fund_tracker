import pandas as pd 
import os
import sys
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src', 'data_processing')))

from load_data import load_mutual_fund_data

def test_load_mutual_fund_data():
    data = load_mutual_fund_data("datasets/input_data.csv")
    assert isinstance(data, pd.DataFrame)