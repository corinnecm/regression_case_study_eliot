import pandas as pd
from zipfile import ZipFile

zf = ZipFile('../data/Train.zip')

df = pd.read_csv('../data/Train.csv')

year = df['YearMade']
year = year[year != 1000]

price_v_year = df[['SalePrice', 'YearMade']]

prices = train['SalePrice']

def get_sale_mon_yr(data):
    data['sale_date'] = pd.to_datetime(data['saledate'])
    data['sale_year'] = pd.DatetimeIndex(data['sale_date']).year
    data['sale_month'] = pd.DatetimeIndex(data['sale_date']).month
    data.drop('saledate', axis=1)

get_saledate_mon_yr(df)

df.head()
