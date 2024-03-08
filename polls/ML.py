import os
import pandas as pd
import sys
sys.path.append(r"C:\Users\acer\Desktop\Projects\ML-Project")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
from polls.models import P206_c, l90_c, Pride_c
application = get_wsgi_application()
from django.db import connection
# Machine Learning
from operator import ne
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import mysql.connector



mydb = mysql.connector.connect(user='root', password='sh.bisto5',
                               host='localhost',
                               database='fin5_jadidb')
cursor = mydb.cursor()


# # پژو، 206
def m_206(mile, mod, trim):
    # cursor.execute("SELECT id, mileage, model, trim, price FROM polls_p206_c")
    cursor.execute("SELECT id, mileage, model, trim, price FROM polls_p206_c")
    rows = cursor.fetchall()

    db = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    X = db.drop(columns=['id','price'])
    y = db['price']
    ls = []

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a random forest regressor object
    model = RandomForestRegressor()
    model.fit(X, y)
    new = model.predict([[mile, mod, trim]])

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print('Model Accuracy:', score)
    ls.append(new[0])
    ls.append(score)
    return ls

# رنو، تندر 90
def m_l90(mile,mod,trim):
    cursor.execute("SELECT id, mileage, model, trim, price FROM polls_l90_c")
    rows = cursor.fetchall()

    db = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    X = db.drop(columns=['id', 'price'])
    y = db['price']
    ls = []

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a random forest regressor object
    model = RandomForestRegressor()
    model.fit(X, y)
    new = model.predict([[mile, mod, trim]])
    print(new)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print('Model Accuracy:', score)
    ls.append(new[0])
    ls.append(score)
    return ls


def m_pride(mile, mod, trim):
    cursor.execute("SELECT id, mileage, model, trim, price FROM polls_pride_c")
    rows = cursor.fetchall()
    db = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])    
    X = db.drop(columns=['id','price'])
    ls = []
    y = db['price']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a random forest regressor object
    model = RandomForestRegressor()
    model.fit(X, y)
    new = model.predict([[mile, mod, trim]])
    # print(new)
    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    # print('Model Accuracy:', score)
    ls.append(new[0])
    ls.append(score)
    return ls

# print(m_206(170,13,300)[0])
# print(m_l90(170,13,300)[0])
# print(m_pride(170,13,300)[0])
# print(m_206(170,13,300)[1])
# print(m_l90(170,13,300)[1])
# print(m_pride(170,13,300)[1])