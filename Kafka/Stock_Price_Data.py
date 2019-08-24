import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle

data = pd.read_csv('Data/GOOG (1).csv')
data.drop(columns=['Adj Close','Volume','Date'], inplace=True)
y = data['Close']
X = data.drop(columns='Close')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
pred = regressor.predict(X_test)
r2_score(pred, y_test)
filename = 'model/model.pickle'
pickle.dump(regressor, open(filename, 'wb'))