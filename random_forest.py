import os
import json
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Проверяем, есть ли dataset.csv
if not os.path.exists("dataset.csv"):
    raise FileNotFoundError("dataset.csv not found. Make sure it is uploaded to the server.")

# Загружаем датасет
df = pd.read_csv("dataset.csv")

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(df["task"], df["languages"], test_size=0.2, random_state=42)

# Обучение модели
vectorizer = TfidfVectorizer()
clf = RandomForestClassifier(n_estimators=100, random_state=42)
pipeline = make_pipeline(vectorizer, clf)
pipeline.fit(X_train, y_train)

# Оценка точности
predictions = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# API на Flask
app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    task = data.get("task", "")
    prediction = pipeline.predict([task])[0]
    return jsonify({"languages": prediction.split()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


