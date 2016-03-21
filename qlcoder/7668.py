import pandas as pd
from string import ascii_lowercase as al
data = pd.read_csv('train.txt')

a = {i:{} for i in range(2,10)}
for index , key , nums , fre in data.itertuples():
    a[nums].setdefault(key,0)
    a[nums][key] += fre

b = {}
fileb = open('seq.txt','r').read()
for x in al:
    for y in al:
        b[x+y] = fileb.count(x+y)

ans = 'zh'

data = list(map(int,['6','3','5', '7', '5', '3', '5', '4', '8', '6', '4', '3', '8', '6', '6', '4', '5', '2', '5', '3', '6', '6', '2', '3']))

for index in range(2,len(data)):
    maxp = 0
    t = ''
    for x in al:
        tp = a[data[index-1]][ans[-1]] * a[data[index]][x] * b[ans[-1]+x]
        if tp > maxp:
            maxp = tp
            t = x
    ans += t