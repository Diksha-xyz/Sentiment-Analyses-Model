
# Sentiment Analysis Model

This project involves building a sentiment analysis model to classify Twitter data into **Positive**, **Negative**, and **Neutral** categories. The model is built using **Logistic Regression** and leverages **TF-IDF** for text vectorization.

The model has been optimized using **GridSearchCV** to find the best hyperparameters. It is then deployed using **Streamlit** to create an interactive web application where users can input tweets and see the predicted sentiment in real-time.

## Key Features:
- Text preprocessing (removal of URLs, mentions, hashtags, punctuation, and digits).
- TF-IDF vectorization with bigrams.
- Hyperparameter tuning using **GridSearchCV**.
- Sentiment classification into **Positive**, **Negative**, and **Neutral**.
- Interactive web app built using **Streamlit** for real-time sentiment prediction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-twitter.git
   cd sentiment-analysis-twitter
# Clone the repository
git clone https://github.com/your-username/sentiment-analysis-twitter.git
cd sentiment-analysis-twitter

# Create a virtual environment (optional but recommended)
python -m venv venv

# On macOS/Linux, activate the virtual environment
source venv/bin/activate

# On Windows, activate the virtual environment
# venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
