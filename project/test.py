import os
import glob

print("Running Test.py")
print()
print('Testing if we have datasets and the preprocessed files')
print()

data_files = glob.glob('../data/*')

files1 = files2 = files3 = all_files = False

print()
print('================================= Testing Files 1  =================================')
print()

if '../data/time-series-air-quality-data-of-india-2010-2023' in data_files:
        if len(glob.glob('../data/time-series-air-quality-data-of-india-2010-2023/*')) == 454:
            files1 = True
            print('Data Files 1 Exists')
else:
    print('Files 1 not found')
    
print()
print('================================= Testing Files 1 Completed ========================')
print()

print('================================= Testing Files 2  =================================')
print()

if '../data/historicalweatherdataforindiancities' in data_files:
        if len(glob.glob('../data/historicalweatherdataforindiancities/Temperature_And_Precipitation_Cities_IN/*')) == 9:
            files2 = True
            print('Data Files 2 Exists')
else:
    print('Files 2 not found')

print()
print('================================= Testing Files 2 Completed ========================')
print()

print()
print('================================= Testing Files 3  =================================')
print()

if '../data/city_wise_csv' in data_files:
        if len(glob.glob('../data/city_wise_csv/*')) == 6:
            files3 = True
            print('Preprocessed and Merged Files Exists')
else:
    print('Merged Files not found')

print()
print('================================= Testing Files 3 Completed ========================')
print()
            
print()
            
if files1 and files2 and files3:
    all_files = True
    print('All Files Exist')
else:
    if files1 == False:
        print('Data Files 1 Does not Exist')
    if files1 == False:
        print('Data Files 2 Does not Exist')
    if files3 == False:
        print('Preprocessed and Merged Files Does not Exist')
        
print()
print('================================= All Tests Completed ==============================')
print()