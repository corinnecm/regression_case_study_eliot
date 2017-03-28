import pandas as pd
from zipfile import ZipFile

#zf = ZipFile('../data/Train.zip')

df = pd.read_csv('../data/Train.csv')

def clean_year_made(data):
   data = data[(data['YearMade'] > 1940) & (data['YearMade'] <= 2017)]
   return data

#price_v_year = df[['SalePrice', 'YearMade']]

#prices = df['SalePrice']

df = df.drop(['SalesID','MachineID'],1)

df = df.drop(['fiModelDesc','fiSecondaryDesc','fiModelSeries','fiModelDescriptor'],1)

#df = df.drop(['datasource','ModelID', 'fiProductClassDesc','ProductGroupDesc', 'UsageBand'],1)

df = df.drop(['datasource','ModelID', 'fiProductClassDesc','ProductGroupDesc', 'MachineHoursCurrentMeter'],1)


machine_conf = ['Drive_System',
      'Enclosure', 'Forks', 'Pad_Type', 'Ride_Control', 'Stick',
      'Transmission', 'Turbocharged', 'Blade_Extension', 'Blade_Width',
      'Enclosure_Type', 'Engine_Horsepower', 'Hydraulics', 'Pushblock',
      'Ripper', 'Scarifier', 'Tip_Control', 'Tire_Size', 'Coupler',
      'Coupler_System', 'Grouser_Tracks', 'Hydraulics_Flow', 'Track_Type',
      'Undercarriage_Pad_Width', 'Stick_Length', 'Thumb',
      'Pattern_Changer', 'Grouser_Type', 'Backhoe_Mounting', 'Blade_Type',
      'Travel_Controls', 'Differential_Type', 'Steering_Controls']


for col in machine_conf:
   df[col] = df[col].isnull().astype(int)

def get_saledate_mon_yr(data):
   data['sale_date'] = pd.to_datetime(data['saledate'])
   data['sale_year'] = pd.DatetimeIndex(data['sale_date']).year
   data['sale_month'] = pd.DatetimeIndex(data['sale_date']).month
   data = data.drop(['sale_date','saledate'],1)
   return data

def drop_null_productsize(df):
   df = df[~df['ProductSize'].isnull()]
   return df

def drop_null_auctioneer(df):
   df = df[~df['auctioneerID'].isnull()]
   df['auctioneerID'] = df['auctioneerID'].apply(str)
   return df

def drop_null_machine(df):
   df = df[~df['MachineHoursCurrentMeter'].isnull()]
   return df

def drop_null_usage(df):
   df = df[~df['UsageBand'].isnull()]
   return df

df = clean_year_made(df)
df = drop_null_productsize(df)
df = drop_null_auctioneer(df)
#df = drop_null_machine(df)
df = drop_null_usage(df)
df = get_saledate_mon_yr(df)

df_full = df

df = df.drop(machine_conf,1)

prices = df['SalePrice']

## Getting and cleaning DF TEST

df_test = pd.read_csv('../data/test.csv')

df_test = df_test.drop(machine_conf,1)
df_test = df_test.drop(['SalesID','MachineID'],1)

df_test = df_test.drop(['fiModelDesc','fiSecondaryDesc','fiModelSeries','fiModelDescriptor'],1)

df_test = df_test.drop(['datasource','ModelID', 'fiProductClassDesc','ProductGroupDesc', 'MachineHoursCurrentMeter'],1)

df_test = clean_year_made(df_test)
df_test = drop_null_productsize(df_test)
df_test = drop_null_auctioneer(df_test)
df_test = drop_null_usage(df_test)
df_test = get_saledate_mon_yr(df_test)
