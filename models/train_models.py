import pandas as pd 
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
import joblib

def build_linear_regression():
    df = pd.read_csv('data/houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "models/linear_regression.joblib")

def build_logistic_regression():
    df = pd.read_csv('data/houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = (df['price'] > df['price'].median()).astype(int)
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, "models/logistic_regression.joblib")

def build_decision_tree():
    df = pd.read_csv('data/houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = (df['price'] > df['price'].median()).astype(int)
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "models/decision_tree.joblib")
    
build_linear_regression()
build_logistic_regression()
build_decision_tree()