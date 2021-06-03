import pandas as pd
from functools import reduce

df1 = pd.read_csv('apims-2005-2017.csv')
df2 = pd.read_csv('apims-2018-now.csv')

df = reduce(lambda left,right: pd.merge(left,right,how='outer'), [df1,df2])

combine_arr = [
    ['ILP Miri', 'Miri'],
    ['Presint 18', 'Putrajaya'],
    ['Kulim Hi-Tech', 'Kulim']
]

for i in combine_arr:
    col1 = [i[1]]
    col2 = [i[0]]
    df[col1] = df[col1].combine_first(pd.DataFrame(df[col2].values,columns=col1))
    df = df.drop(col2,axis=1)

df = df.set_index('Time')
df = df.sort_index(axis=0)
df = df.sort_index(axis=1)

df.to_csv('APIMS-final.csv',date_format='%Y-%m-%d %H:%M')

with open('APIMS-final.csv', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('.0', '').replace(',0,0,', ',,,').replace(',0,', ',,')

with open('APIMS-final.csv', 'w') as file:
  file.write(filedata)

