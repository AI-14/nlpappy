from fastapi import FastAPI
from typing import Dict
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
from src.text_utility import clean_text
import warnings
import numpy as np


app = FastAPI()


@app.get('/')
def main_page() -> Dict[str, str]:
    """ Method for displaying basic info about the API. """

    info = 'NLPAppy - A REST API for covid19 (binary) sentiment prediction and toxic comments tweet (multilabel) prediction.'
    usage = 'Follow this link: www.github/AI-14/NLPAppy'
    return {
        'INFO': info,
        'USAGE': usage
    }


@app.get('/covid/{text_original}')
def get_covid_sentiment(text_original: str) -> Dict[str, str]:
    """ Method for predicting sentiment of a tweet related to covid19. """

    warnings.filterwarnings('ignore')

    # Cleaning the text and making it ready for vectorization.
    text = clean_text(text_original)
    text = ' '.join(ch for ch in text)

    # Using tfidf vectorizer on the cleaned text.
    tf_idf = pickle.load(open('C:\\Users\\amaan\\Python Projects\\NLPAppy\\src\\models\\tf_idf.pkl', 'rb'))
    vectorized_text = tf_idf.transform([text])

    # Using the machine learning model for prediction.
    model = pickle.load(open('C:\\Users\\amaan\\Python Projects\\NLPAppy\\src\\models\\linearSVC.pkl', 'rb'))
    prediction = model.predict(vectorized_text)

    # Decoding the prediction.
    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'

    return {
        'Original Text': text_original,
        'Sentiment Predicted': sentiment
    }


@app.get('/toxiccomment/{text_original}')
def get_toxic_comment_levels(text_original: str) -> Dict[str, str]:
    """ Method for predicting the toxic labels of a comment."""

    warnings.filterwarnings('ignore')

    # Cleaning the text and making it ready for vectorization.
    text = clean_text(text_original)
    text = ' '.join(ch for ch in text)
    vec_text = np.asarray([text])

    # Turning the cleaned text into sequences and then padding it.
    tokenizer = pickle.load(open('C:\\Users\\amaan\\Python Projects\\NLPAppy\\src\\models\\tokenizer.pkl', 'rb'))
    text_to_seq = tokenizer.texts_to_sequences(vec_text)
    padded_seq = pad_sequences(text_to_seq, maxlen=200, padding='post')

    # Using the model to predict the labels.
    model = load_model('C:\\Users\\amaan\\Python Projects\\NLPAppy\\src\\models\\toxic_comm_model.h5')
    prediction = model.predict(padded_seq)

    # Decoding the prediction.
    for i in range(prediction.shape[0]):
        for j in range(6):
            if prediction[i][j] >= 0.5:
                prediction[i][j] = 1
            else:
                prediction[i][j] = 0

    toxic = str(prediction[0][0])
    severe_toxic = str(prediction[0][1])
    obscene = str(prediction[0][2])
    threat = str(prediction[0][3])
    insult = str(prediction[0][4])
    indentity_hate = str(prediction[0][5])

    return {
        'Original Text': text_original,
        'Label meaning': '1 = YES, 0 = NO',
        'Toxic?': toxic,
        'Severe Toxic?': severe_toxic,
        'Obscene?': obscene,
        'Threat?': threat,
        'Insult?': insult,
        'Identity Hate?': indentity_hate
    }