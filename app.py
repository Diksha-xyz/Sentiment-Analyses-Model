import streamlit as st
import pandas as pd
import re
import string
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ---------- Load model and vectorizer ----------
@st.cache_resource
def load_model():
    model = joblib.load("logistic_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# ---------- Preprocess Function ----------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)  
    text = re.sub(r'\@w+|\#', '', text) 
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = re.sub(r'\d+', '', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

# ---------- Streamlit App ----------

st.title("💬 Twitter Sentiment Analyzer")
st.write("Enter a tweet below to analyze its sentiment using a trained Logistic Regression model.")

user_input = st.text_area("Enter Tweet Text:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = preprocess(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        label_map = {1: "Positive 😊", 0: "Neutral 😐", -1: "Negative 😠"}
        st.subheader("Predicted Sentiment:")
        st.success(label_map[prediction])
