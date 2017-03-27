import pandas as pd
from zipfile import ZipFile

zf = ZipFile('data/Train.zip')

df = pd.read_csv('data/Train.csv')

year = df['YearMade']
year = year[year != 1000]

def clean_year_made(data):
    data = data[(data['YearMade'] > 1920) & (data['YearMade'] <= 2017)]
    return data


price_v_year = df[['SalePrice', 'YearMade']]
