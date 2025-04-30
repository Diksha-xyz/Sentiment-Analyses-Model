
# Sentiment Analysis Model

This project involves building a sentiment analysis model to classify Twitter data into **Positive**, **Negative**, and **Neutral** categories. The model is built using **Logistic Regression** and leverages **TF-IDF** for text vectorization.

The model has been optimized using **GridSearchCV** to find the best hyperparameters. It is then deployed using **Streamlit** to create an interactive web application where users can input tweets and see the predicted sentiment in real-time.

## Key Features:
- Text preprocessing (removal of URLs, mentions, hashtags, punctuation, and digits).
- TF-IDF vectorization with bigrams.
- Hyperparameter tuning using **GridSearchCV**.
- Sentiment classification into **Positive**, **Negative**, and **Neutral**.
- Interactive web app built using **Streamlit** for real-time sentiment prediction.

## Requirements
The following Python libraries are required to run the project:

- scikit-learn
- pandas
- numpy
- nltk
- streamlit

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Diksha-xyz/sentiment-analysis-twitter.git
   cd sentiment-analysis-twitter(https://github.com/Diksha-xyz/Sentiment-Analyses-Model.git)

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
3. **Run the application:**

   ```bash
   streamlit run app.py
4. **Access the application:**

Open your browser and navigate to [https://pharmamap-health.netlify.app](https://pharmamap-health.netlify.app)

## Model Details

- **Logistic Regression**: Used for classification to categorize tweets into Positive, Negative, or Neutral sentiments.
  
- **TF-IDF Vectorizer**: Converts text data into numerical form, allowing the machine learning model to work with the text data effectively.

- **GridSearchCV**: Optimizes hyperparameters for the best Logistic Regression model, ensuring improved accuracy and performance.

