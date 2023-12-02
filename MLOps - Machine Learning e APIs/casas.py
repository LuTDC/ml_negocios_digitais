import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

NOME_MODELO = 'modelo.sav'

def treinar_modelo():
    df = pd.read_csv('casas.csv')
    print(df.head())

    X = df.drop(columns=['preco'], axis=1)
    y = df['preco']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42)

    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)

    pickle.dump(linear_regression, open(NOME_MODELO, 'wb'))

def prever_preco(X):
    if os.path.exists(NOME_MODELO):
        modelo = pickle.load(open(NOME_MODELO, 'rb'))
        return modelo.predict(X)    
    return [-1]