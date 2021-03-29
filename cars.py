import os
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

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

sns.histplot(df['Price'], color = 'black')


##################
# Train/test split
num_training = int(0.8 * df['Price'].count())
num_test = df['Price'].count() - num_training

# Training data
X_train = np.array(df['Mileage'][:num_training]).reshape((num_training,1))
y_train = np.array(df['Price'][:num_training])

# Test data
X_test = np.array(df['Mileage'][num_training:]).reshape((num_test,1))
y_test = np.array(df['Price'][num_training:])

# Create linear regression object
from sklearn import linear_model

linear_regressor = linear_model.LinearRegression()

# Train the model using the training sets
linear_regressor.fit(X_train, y_train)
y_test_pred = linear_regressor.predict(X_test)

plt.scatter(X_test, y_test, color='red', marker = '.', linewidths=1)
plt.plot(X_test, y_test_pred, color='black', linewidth=1)
plt.xticks(())
plt.yticks(())
plt.show()


import sklearn.metrics as sm

print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred), 2))
print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred), 2))
print("Explain variance score =", round(sm.explained_variance_score(y_test, y_test_pred), 2))
print("R2 score =", round(sm.r2_score(y_test, y_test_pred), 2))

output_model_file = '3_model_linear_regr.pkl'

with open(output_model_file, 'wb') as f:
    pickle.dump(linear_regressor, f)

with open(output_model_file, 'rb') as f:
    model_linregr = pickle.load(f)

y_test_pred_new = model_linregr.predict(X_test)
print("\nNew mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_new), 2))

