import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def load_data():
    conn = sqlite3.connect("results.db")
    df = pd.read_sql_query("SELECT balance, winnings FROM game_results", conn)
    conn.close()
    return df

def train_model():
    df = load_data()
    
    if df.shape[0] < 10:  # Ei tarpeeksi dataa vielä
        print("Not enough data to train the model")
        return None

    X = df[['balance']]
    y = df['winnings']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test) * 100
    print(f"Model trained with accuracy: {accuracy:.2f}%")
    
    return model

def predict_winnings(balance):
    model = train_model()
    if model:
        # 🛠️ Korjataan varoitus muuntamalla input `DataFrameksi`
        import numpy as np
        input_data = pd.DataFrame(np.array(balance).reshape(-1, 1), columns=['balance'])
        prediction = model.predict(input_data)[0]
        return max(0, prediction)  # Estetään negatiiviset voittoennusteet
    return None
