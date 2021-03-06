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
    temp['filename'] = file
    df = df.append(temp)

df.isnull().sum()
# Checking for null values in the Dataframe
plt.subplots()
msno.matrix(df, figsize=(10, 10))
plt.subplots()
msno.bar(df, figsize=(12, 8))

# TODO: какие вопросы по датасету (год выпуска?), что посмотреть: изменения цен с каждым годом пробега
# TODO: установить формат колонки category для которых это логично.
# TODO: гистограмма, bar chart
# TODO: почему выводится пустой график
