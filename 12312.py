import os
import pandas as pd


df = pd.DataFrame(columns = ['file', 'owner', 'location'])

path = 'Z:/Сотрудники'
ans = []
for root, dir, file in os.walk(path):
    for filename in file:
        ans.append(filename)
data = [[filename, dir, root] for root, dir, file in os.walk(path) for filename in file]

df = pd.DataFrame()
df = df.from_records(data)
df.to_excel('folders.xlsx')