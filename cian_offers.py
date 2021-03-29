import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = 'C:/Users/cth/Downloads/offers.xlsx'

pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
pd.set_option('display.precision', 4)
pd.set_option('expand_frame_repr', True)

df = pd.read_excel(path)
df.columns
names = ['ID  объявления', 'Тип', 'Площадь', 'Класс', 'Адрес', 'Цена',  'Телефоны', 'Описание', 'Ссылка на объявление']
df_new = df[names].copy()
df_new.columns = ['id', 'type', 'sq', 'class', 'adress', 'price', 'contact', 'desc', 'link']
df_new.set_index('id', inplace = True)

df_new['price'].unique()