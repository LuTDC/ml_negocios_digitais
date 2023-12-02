import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def treinar_modelo():
    df = pd.read_csv('casas.csv')
    print(df.head())

    X = df.drop(columns=['preco'], axis=1)
    y = df['preco']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42)

    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)

    return linear_regression

def prever_preco(modelo, X):
    return modelo.predict(X)