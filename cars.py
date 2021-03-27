import os
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Creating dictionary for all columns names in the dataset
columns = {'Model': 'model',
           'Year': 'year',
           'Price': 'price',
           'Transmission': 'transmission',
           'Fuel type': ['fuel type', 'fuelType', 'fuel type 2'],
           'Mileage': ['mileage', 'mileage2'],
           'Engine size': ['engine size', 'engine size2', 'engineSize'],
           'Tax': ['tax', 'tax(£)']}

# Combining all files into DataFrame
path = 'Datasets/uk_used_cars'
df = pd.DataFrame()
for file in os.listdir(path):
    temp = pd.read_csv(os.path.join(path, file), names=columns, header=None, index_col=False, skiprows=1)
    temp['Brand'] = file.split(".")[0]
    df = df.append(temp)

# Checking for null values in the Dataframe
plt.subplots()
msno.matrix(df, figsize=(10, 10))
plt.subplots()
msno.bar(df, figsize=(12, 8))

# Drop null values
df.dropna(subset=['Mileage', 'Year'], inplace=True)

# установить формат колонки category для которых это логично.
categorical=['Model', 'Transmission', 'Fuel type', 'Brand']
df[categorical]=df[categorical].astype('category')
numeric=['Price','Mileage','Tax']
df['Price']=df['Price'].str.replace('£','')
df['Price']=df['Price'].str.strip()
df['Price']=df['Price'].str.replace(',','')
df[numeric]=df[numeric].astype('float')

# TODO: какие вопросы по датасету (год выпуска?), что посмотреть: изменения цен с каждым годом пробега
# TODO: engine size проверить как собираются данные, попадают текстовые значения, проверить уникальные значения
# TODO: гистограмма, bar chart
# TODO: почему выводится пустой график
