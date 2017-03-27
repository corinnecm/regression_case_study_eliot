import pandas as pd
from zipfile import ZipFile

zf = ZipFile('../data/Train.zip')

df = pd.read_csv('../data/Train.csv')

year = df['YearMade']
year = year[year != 1000]

price_v_year = df[['SalePrice', 'YearMade']]

prices = train['SalePrice']

df = df.drop(['fiModelDesc','fiSecondaryDesc','fiModelSeries','fiModelDescriptor'],1)

df = df.drop(['datasource','ModelID', 'ProductClassDesc','ProductGroupDesc'])

def get_saledate_mon_yr(data):
    data['sale_date'] = pd.to_datetime(data['saledate'])
    data['sale_year'] = pd.DatetimeIndex(data['sale_date']).year
    data['sale_month'] = pd.DatetimeIndex(data['sale_date']).month

def clean_year_made(data):
    data = data[(data['YearMade'] > 1940) & (data['YearMade'] <= 2017)]
    return data

def drop_null_auctioneer(df):
    df = df.dropna(subset=['auctioneerID'])
    return df

def drop_null_machine(df):
    df = df.dropna(subset=['MachineHoursCurrentMeter'])
    return df

get_saledate_mon_yr(df)
clean_year_made(df)
drop_null_auctioneer(df)
drop_null_machine(df)

def get_sale_mon_yr(data):
    data['sale_date'] = pd.to_datetime(data['saledate'])
    data['sale_year'] = pd.DatetimeIndex(data['sale_date']).year
    data['sale_month'] = pd.DatetimeIndex(data['sale_date']).month
    data.drop('saledate', axis=1)

get_saledate_mon_yr(df)

df.head()
