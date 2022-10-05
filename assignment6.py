import pandas as pd
import requests
import os
import sys
import time

cwd = os.getcwd()

#pulling data from public source
r = requests.get('https://health.data.ny.gov/resource/d54z-enu8.json')
r_data = r.json() ## load request as json
## load into dataframe
r_data = pd.DataFrame(r_data)

r_data.to_csv('./blood_lead_testing.csv')

# create a new dictionary with dummy data
data = r_data

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/assignment6_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))

#in Vm instead of cwd, we used direct file path /home/user/crontab/assignment6_ 
# to make sure cronjobs can find correct path.