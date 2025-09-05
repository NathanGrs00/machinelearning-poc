#numpy is een bibliotheek voor numerieke berekeningen in Python
import numpy as np
#sklearn is een machine learning bibliotheek, we importeren hier een lineair regressie model
from sklearn.linear_model import LinearRegression

# Deze functie traint een lineair regressiemodel met de gegeven x en y waarden
def train_and_predict(x, y, val):
    # Zet de lijsten om naar numpy arrays, omdat sklearn met numpy arrays werkt
    x = np.array(x).reshape(-1, 1) # Reshape zodat het een 2D array is, wat sklearn verwacht
    y = np.array(y)
    # Maak een lineair regressiemodel aan
    model = LinearRegression()
    # Voeg de numpy arrays toe aan het model
    model.fit(x, y)
    # Gebruik het getrainde model om een voorspelling te doen voor de nieuwe waarde 'val'
    return model.predict(np.array([[val]]))[0] # [0] staat voor het eerste element.
