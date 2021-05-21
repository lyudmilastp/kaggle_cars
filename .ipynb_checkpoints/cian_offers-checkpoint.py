import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = 'Copy of 54790.xlsx'

pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
pd.set_option('precision', 4)
pd.set_option('expand_frame_repr', True)

df = pd.read_excel(path)
names = ['date', 'price', 'tel', 'operator', 'type', 'adress', 'desc', 'category', 'category_sub', 'link',
       'link_images', 'geo_l', 'geo_w', 'count', 'floor', 'floors', 'square', 'square_dinner', 'square_live', 'square_land',
       'year', 'type']
df.columns = names
df.set_index('date', inplace = True)




df['category_sub'].value_counts()
grouped_cat = df.groupby('category_sub').aggregate({'price': ['sum', 'mean'], 'square' : ['sum','mean'] })


for index, i in enumerate(grouped_cat):
       plt.subplot(3,2,index + 1)
       plt.bar(grouped_cat[i].values, grouped_cat[i].index)