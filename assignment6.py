import pandas as pd
import requests
import os
import sys
import time

r = requests.get('https://health.data.ny.gov/resource/d54z-enu8.json')
r_data = r.json() ## load request as json
## load into dataframe
df = pd.read_json(r_data, orient='index')

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# create a new dictionary with dummy data
data = {'a': 1, 'b': 2, 'c': 3}

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))

# /Library/Frameworks/Python.framework/Versions/3.10/bin/python3