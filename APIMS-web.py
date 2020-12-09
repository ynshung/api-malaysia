import pandas as pd
import numpy as np
from urllib import request
from pathlib import Path
import re

df2 = pd.DataFrame()

date = pd.to_datetime('2018/01/01 2300', format='%Y/%m/%d %H%M')

def returnFile(url=False):
    if url:
        return date.strftime(format='%Y/%m/%d/%H%M') + '.json'
    else:
        return date.strftime(format='%Y-%m-%d-%H%M') + '.json'

def returnURL():
    return 'http://apims.doe.gov.my/data/public_v2/CAQM/hours24/' + returnFile(True)

def getJSON():
    fpath = 'cache/' + returnFile()
    cache_file = Path(fpath)
    if not cache_file.is_file():
        print("Requesting " + returnURL())
        request.urlretrieve(returnURL(),fpath)
    return fpath

def clean(x):
    try:
        return int(re.sub('\D', '', str(x)))
    except:
        return np.nan

while date <= pd.to_datetime('now'):
    print('Processing ' + returnFile())
    try:
        json = pd.read_json(getJSON())
    except:
        print('Error occured')
        date += pd.DateOffset(hours=8)
        continue

    try:
        df = json['24hour_api'].apply(pd.Series)
    except:
        df = json['24hour_api_apims'].apply(pd.Series)

    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    df = df.set_index('Location')
    df = df.drop(columns='State',axis=1)
    df = df.applymap(clean)

    df = df.transpose()
    df = df.astype(np.float16)

    ls = list(df.index)
    passed = False
    for i,v in enumerate(ls):
        if v == '12:00AM':
            passed = True
        if passed:
            ls[i] = date.strftime(format='%Y/%m/%d') + ' ' + ls[i]
        else:
            ls[i] = (date-pd.DateOffset(1)).strftime(format='%Y/%m/%d') + ' ' + ls[i]
    df.index = pd.to_datetime(ls)

    df2 = df2.combine_first(df)
    
    date += pd.DateOffset(hours=8)
    #if date == pd.to_datetime('2019/10/24 2300'):
    #    date -= pd.DateOffset(hours=1)

df2.to_csv('apims-2018-2020.csv',date_format='%Y-%m-%d %H:%M')

with open('apims-2018-2020.csv', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('.0', '').replace(',0,0,', ',,,').replace(',0,', ',,')
with open('apims-2018-2020.csv', 'w') as file:
  file.write(filedata)

print("Saved! Operation complete.")
