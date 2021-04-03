import os
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics as sm
from sklearn import linear_model

#: 1. Dataset manipulations
# Creating dictionary for all columns names in the dataset
columns = {'Model': 'model',
           'Year': 'year',
           'Price': 'price',
           'Transmission': 'transmission',
           'Mileage': ['mileage', 'mileage2'],
           'Fuel type': ['fuel type', 'fuelType', 'fuel type 2'],
           'Tax': ['tax', 'tax(£)'],
           'Engine size': ['engine size', 'engine size2', 'engineSize']}

# Combining all files into DataFrame
path = 'Datasets/uk_used_cars'
df = pd.DataFrame()
for file in os.listdir(path):
    if file.find('unclean')!=-1:
        pass
    else:
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

# Set categorical type, plotting with categorical data
categorical = ['Transmission', 'Fuel type', 'Brand']
df[categorical] = df[categorical].astype('category')

# v_1 with matplotlib
by_fuel_type = df.groupby('Fuel type').agg({'Fuel type':'count'}).rename(columns={'Fuel type':'values'}).reset_index().sort_values(by='values', ascending=False)
plt.subplots()
plt.bar(by_fuel_type['Fuel type'], by_fuel_type['values'])

# v_2 with seaborn
plt.subplots()
sns.countplot(x='Brand',
              data=df,
              order=df['Brand'].value_counts().index,
              palette='mako')

# Add column with period of use
df['Years of use'] = 2018 - df['Year']
conditions = [df['Years of use']<3, df['Years of use']<6, df['Years of use']<10, df['Years of use']>=10]
outputs = ['less than 3', 'from 3 to 6', 'from 6 to 10', 'more than 10']
df['Period of use'] = np.select(conditions, outputs)

# Pivot table
aver_price = df.pivot_table(index='Brand',
               columns='Period of use',
               values='Price',
               fill_value=0,)

# Distribution of prices by brands
grouped = df.groupby(['Period of use', 'Brand'])['Price'].mean().reset_index()

plt.subplots()
sns.boxplot(x='Brand', y='Price', data=grouped)
plt.title('Average price by brands')


# TODO: изменения цен с каждым годом пробега
# TODO: почему выводится пустой график

#: 2. Linear regression
# корреляционная матрица
cor_mat = df.corr()
plt.subplots()
sns.heatmap(cor_mat, vmin=-1, vmax = 1, cmap='coolwarm', annot=True)

# гистрограмма по цене
plt.subplots()
sns.histplot(df['Price'], color = 'black')

# Train/test split
num_training = int(0.8 * df['Price'].count())
num_test = df['Price'].count() - num_training

# Training data
X_train = np.array(df['Year'][:num_training]).reshape((num_training,1))
y_train = np.array(df['Price'][:num_training])

# Test data
X_test = np.array(df['Year'][num_training:]).reshape((num_test,1))
y_test = np.array(df['Price'][num_training:])

# Create linear regression object
linear_regressor = linear_model.LinearRegression()

# Train the model using the training sets
linear_regressor.fit(X_train, y_train)
y_test_pred = linear_regressor.predict(X_test)

plt.subplots()
plt.scatter(X_test, y_test, color='red', marker = '.', linewidths=1)
plt.plot(X_test, y_test_pred, color='black', linewidth=1)
plt.xticks(())
plt.yticks(())
plt.show()

print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print("Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2))
print("R2 score =", round(sm.r2_score(y_test, y_test_pred), 2))
