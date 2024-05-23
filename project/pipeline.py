import os
os.environ['KAGGLE_USERNAME'] = 'nippuunn' 
os.environ['KAGGLE_KEY'] = '63005089f5d24ae24b60a9fbab7725b6' 

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
