import os
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

import kaggle
import time

# Not to worry the above account is not my main account :)

dataset1 = 'abhisheksjha/time-series-air-quality-data-of-india-2010-2023' 
dataset2 = 'vanvalkenberg/historicalweatherdataforindiancities' 

folder1 = f"../data/{dataset1.split('/')[-1]}/"
folder2 = f"../data/{dataset2.split('/')[-1]}/"

os.mkdir(folder1)
os.mkdir(folder2)
print('Folders created at /data')

print('Downloading Datasets')

kaggle.api.dataset_download_files(dataset1, path=folder1, unzip=True)
time.sleep(1)
kaggle.api.dataset_download_files(dataset2, path=folder2, unzip=True)
