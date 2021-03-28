import os
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
pd.set_option('display.precision', 4)
pd.set_option('expand_frame_repr', True)


# Creating dictionary for all columns names in the dataset
columns = {'Model': 'model',
           'Year': 'year',
           'Price': 'price',
           'Transmission': 'transmission',
           'Mileage': ['mileage', 'mileage2'],
           'Fuel type': ['fuel type', 'fuelType', 'fuel type 2'],
           'Engine size': ['engine size', 'engine size2', 'engineSize'],
           'Tax': ['tax', 'tax(£)']}

# Combining all files into DataFrame
path = 'Datasets/uk_used_cars'
df = pd.DataFrame()
for file in os.listdir(path):
    if file.find('unclean') != -1:
        pass
    else:
        temp = pd.read_csv(os.path.join(path, file), names=columns, header=None, index_col=False, skiprows=1)
        temp['Brand'] = file.split(".")[0]
        df = df.append(temp)

# Checking for null values in the Dataframe
# plt.subplots()
# msno.matrix(df, figsize=(10, 10))
# plt.subplots()
# msno.bar(df, figsize=(12, 8))

# Drop null values
df.dropna(subset=['Mileage', 'Year'], inplace=True)

# установить формат колонки category для которых это логично.
categorical=['Model', 'Transmission', 'Fuel type', 'Brand']
numeric=['Price','Mileage','Tax']
# df['Price']=df['Price'].str.replace('£','')
# df['Price']=df['Price'].str.strip()
# df['Price']=df['Price'].str.replace(',','')
df[numeric] = df[numeric].astype('float')
df[categorical] = df[categorical].astype('category')
cor_mat = df.corr()
sns.heatmap(cor_mat, vmin=-1, vmax = 1, linecolor='black', linewidths=.1, center = 1)
