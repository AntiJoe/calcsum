import pandas as pd
import numpy as np
import csv

def findrow(x,y):
    dff = df[ (df.X == x) & (df.Y == y) ]
    return [dff.iat[0,0], dff.iat[0,1], dff.S.sum()]

df = pd.read_csv('data.csv') # read in data file
count = len(df.index)

# find unique value pairs in columns X and Y
dfxy = df.drop(columns=['Z','S']) # drop all columns but X and Y
tlist = list(dfxy.to_records(index=False)) # convert to list of tuples
ulist = np.unique(np.array(tlist))         # keep only unique values

outlist = []
for t in ulist:
    x, y = t
    outlist.append(findrow(x, y))

dfout = pd.DataFrame(outlist, columns=['X', 'Y', 'SumS'])
print(dfout)
dfout.to_csv('dfout.csv')

#print(testdf)

#print([testdf.iat[0,0], testdf.iat[0,1], testdf.S.sum()]) 

