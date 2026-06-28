from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

texts = [
    "I love this product, it works great",
    "Absolutely fantastic experience",
    "This is the best purchase I made",
    "Highly recommend this to everyone",
    "I am very happy with the results",
    "This is terrible and broke immediately",
    "Worst purchase I have ever made",
    "Completely disappointed with this",
    "Do not buy this, total waste of money",
    "I hate how this turned out",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB()),
])

model.fit(texts, labels)

joblib.dump(model, "ml_models/sentiment_v1.pkl")
print("Model trained and saved to ml_models/sentiment_v1.pkl")
