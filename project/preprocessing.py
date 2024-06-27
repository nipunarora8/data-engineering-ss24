import pandas as pd
import glob
import os

print('Running Preprocessing.py')

dataset1 = './data/historicalweatherdataforindiancities/Temperature_And_Precipitation_Cities_IN/'
dataset2 = './data/time-series-air-quality-data-of-india-2010-2023/'

files_in_dataset1 = glob.glob(f'{dataset1}*')
files_in_dataset2 = glob.glob(f'{dataset2}*')

### For our analysis, we will only take the metro cities which are Delhi NCR, Mumbai, Bangalore and Chennai

selected_files_in_dataset1 = ['Delhi_NCR_1990_2022_Safdarjung.csv',\
                              'Mumbai_1990_2022_Santacruz.csv',\
                              'Chennai_1990_2022_Madras.csv',\
                              'Bangalore_1990_2022_BangaloreCity.csv',\
                              'Lucknow_1990_2022.csv',\
                              'Rajasthan_1990_2022_Jodhpur.csv']

air_monitoring_stations = pd.read_csv(f'{dataset2}/stations_info.csv')

selected_cities = ['Delhi', 'Mumbai', 'Chennai','Bengaluru', 'Jodhpur', 'Lucknow']

air_monitoring_stations = air_monitoring_stations[air_monitoring_stations['city'].isin(selected_cities)]
air_monitoring_stations = air_monitoring_stations.reset_index()

### Based on the geo location and the availability of the data we have selected some data files that we will study. 

# For the nomenclature, 
# delhi1 means data of city delhi from data source 1
# and delhi2 means data of city delhi from data source 2

delhi1 = pd.read_csv(f'{dataset1}Delhi_NCR_1990_2022_Safdarjung.csv')
mumbai1 = pd.read_csv(f'{dataset1}Mumbai_1990_2022_Santacruz.csv')
chennai1 = pd.read_csv(f'{dataset1}Chennai_1990_2022_Madras.csv')
bangalore1 = pd.read_csv(f'{dataset1}Bangalore_1990_2022_BangaloreCity.csv')
lucknow1 = pd.read_csv(f'{dataset1}Lucknow_1990_2022.csv')
jodhpur1 = pd.read_csv(f'{dataset1}Rajasthan_1990_2022_Jodhpur.csv')

delhi2 = pd.read_csv(f'{dataset2}DL001.csv')
mumbai2 = pd.read_csv(f'{dataset2}MH002.csv')
chennai2 = pd.read_csv(f'{dataset2}TN001.csv')
bangalore2 = pd.read_csv(f'{dataset2}KA001.csv')
lucknow2 = pd.read_csv(f'{dataset2}UP001.csv')
jodhpur2 = pd.read_csv(f'{dataset2}RJ001.csv')

# Filtering data to match date and time

delhi1['time'] = pd.to_datetime(delhi1['time'], format='%d-%m-%Y')
delhi1 = delhi1[delhi1['time'] >= '01-01-2010'].reset_index(drop=True)
delhi1 = delhi1.rename(columns={'time':'date'})

#same for mumbai
mumbai1['time'] = pd.to_datetime(mumbai1['time'], format='%d-%m-%Y')
mumbai1 = mumbai1[mumbai1['time'] >= '01-01-2010'].reset_index(drop=True)
mumbai1 = mumbai1.rename(columns={'time':'date'})

#same for chennai
chennai1['time'] = pd.to_datetime(chennai1['time'], format='%d-%m-%Y')
chennai1 = chennai1[chennai1['time'] >= '01-01-2010'].reset_index(drop=True)
chennai1 = chennai1.rename(columns={'time':'date'})

#same for bangalore
bangalore1['time'] = pd.to_datetime(bangalore1['time'], format='%d-%m-%Y')
bangalore1 = bangalore1[bangalore1['time'] >= '01-01-2010'].reset_index(drop=True)
bangalore1 = bangalore1.rename(columns={'time':'date'})

#same for lucknow
lucknow1['time'] = pd.to_datetime(lucknow1['time'], format='%d-%m-%Y')
lucknow1 = lucknow1[lucknow1['time'] >= '01-01-2010'].reset_index(drop=True)
lucknow1 = lucknow1.rename(columns={'time':'date'})

#same for mumbai
jodhpur1['time'] = pd.to_datetime(jodhpur1['time'], format='%d-%m-%Y')
jodhpur1 = jodhpur1[jodhpur1['time'] >= '01-12-2015'].reset_index(drop=True)
jodhpur1 = jodhpur1.rename(columns={'time':'date'})


delhi2 = delhi2.drop('To Date', axis=1)
mumbai2 = mumbai2.drop('To Date', axis=1)
chennai2 = chennai2.drop('To Date', axis=1)
bangalore2 = bangalore2.drop('To Date', axis=1)
lucknow2 = lucknow2.drop('To Date', axis=1)
jodhpur2 = jodhpur2.drop('To Date', axis=1)

delhi2['From Date'] = pd.to_datetime(delhi2['From Date'])
delhi2['date'] = delhi2['From Date'].dt.date
delhi2 = delhi2.groupby('date').mean().reset_index()
delhi2 = delhi2.drop('From Date',axis=1)
delhi1['date'] = pd.to_datetime(delhi1['date'])
delhi2['date'] = pd.to_datetime(delhi2['date'])
delhi_merged = pd.merge(delhi1, delhi2, on='date')

mumbai2['From Date'] = pd.to_datetime(mumbai2['From Date'])
mumbai2['date'] = mumbai2['From Date'].dt.date
mumbai2 = mumbai2.groupby('date').mean().reset_index()
mumbai2 = mumbai2.drop('From Date',axis=1)
mumbai1['date'] = pd.to_datetime(mumbai1['date'])
mumbai2['date'] = pd.to_datetime(mumbai2['date'])
mumbai_merged = pd.merge(mumbai1, mumbai2, on='date')

chennai2['From Date'] = pd.to_datetime(chennai2['From Date'])
chennai2['date'] = chennai2['From Date'].dt.date
chennai2 = chennai2.groupby('date').mean().reset_index()
chennai2 = chennai2.drop('From Date',axis=1)
chennai1['date'] = pd.to_datetime(chennai1['date'])
chennai2['date'] = pd.to_datetime(chennai2['date'])
chennai_merged = pd.merge(chennai1, chennai2, on='date')

bangalore2['From Date'] = pd.to_datetime(bangalore2['From Date'])
bangalore2['date'] = bangalore2['From Date'].dt.date
bangalore2 = bangalore2.groupby('date').mean().reset_index()
bangalore2 = bangalore2.drop('From Date',axis=1)
bangalore1['date'] = pd.to_datetime(bangalore1['date'])
bangalore2['date'] = pd.to_datetime(bangalore2['date'])
bangalore_merged = pd.merge(bangalore1, bangalore2, on='date')

lucknow2['From Date'] = pd.to_datetime(lucknow2['From Date'])
lucknow2['date'] = lucknow2['From Date'].dt.date
lucknow2 = lucknow2.groupby('date').mean().reset_index()
lucknow2 = lucknow2.drop('From Date',axis=1)
lucknow1['date'] = pd.to_datetime(lucknow1['date'])
lucknow2['date'] = pd.to_datetime(lucknow2['date'])
lucknow_merged = pd.merge(lucknow1, lucknow2, on='date')


jodhpur2['From Date'] = pd.to_datetime(jodhpur2['From Date'])
jodhpur2['date'] = jodhpur2['From Date'].dt.date
jodhpur2 = jodhpur2.groupby('date').mean().reset_index()
jodhpur2 = jodhpur2.drop('From Date',axis=1)
jodhpur1['date'] = pd.to_datetime(jodhpur1['date'])
jodhpur2['date'] = pd.to_datetime(jodhpur2['date'])
jodhpur_merged = pd.merge(jodhpur1, jodhpur2, on='date')

if not os.path.exists('./data/city_wise_csv'):
    os.mkdir('./data/city_wise_csv')

delhi_merged.to_csv('./data/city_wise_csv/delhi_merged.csv',index=False)
mumbai_merged.to_csv('./data/city_wise_csv/mumbai_merged.csv',index=False)
chennai_merged.to_csv('./data/city_wise_csv/chennai_merged.csv',index=False)
bangalore_merged.to_csv('./data/city_wise_csv/bangalore_merged.csv',index=False)
lucknow_merged.to_csv('./data/city_wise_csv/lucknow_merged.csv',index=False)
jodhpur_merged.to_csv('./data/city_wise_csv/jodhpur_merged.csv',index=False)

print('Saved files at ./data/city_wise_csv')
print()