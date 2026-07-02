from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

texts = [
    "I love this product, it works great",
    "Absolutely fantastic experience",
    "This is the best purchase I made",
    "Highly recommend this to everyone",
    "I am very happy with the results",
    "Amazing quality, exceeded expectations",
    "Five stars, will buy again",
    "This is terrible and broke immediately",
    "Worst purchase I have ever made",
    "Completely disappointed with this",
    "Do not buy this, total waste of money",
    "I hate how this turned out",
    "Awful experience, avoid at all costs",
    "Broken on arrival, very unhappy",
]
labels = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", LogisticRegression()),
])

model.fit(texts, labels)
joblib.dump(model, "ml_models/sentiment_v2.pkl")
print("v2 model trained and saved to ml_models/sentiment_v2.pkl")
