# NLPAppy
  ![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python)
  ![Deep Learning](https://img.shields.io/badge/-Deep%20Learning-566be8?style=flat)
  ![Sklearn](https://img.shields.io/badge/-Sklearn-1fb30e?style=flat)
  ![Tensorflow](https://img.shields.io/badge/-Tensorflow-gray?style=flat&logo=tensorflow)
  ![Keras](https://img.shields.io/badge/-Keras-gray?style=flat&logo=keras)
  ![NLTK](https://img.shields.io/badge/-NLTK-f0886c?style=flat)
  ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-black?style=flat&logo=jupyter)
  ![FastAPI](https://img.shields.io/badge/-FastAPI-f0806c?style=flat)

## Description
   A REST API for 2 NLP models capable of predicting sentiments (binary) and mulitlabel classification of a text or a tweet.
   
   1. Covid19 Tweets Sentiment Analysis:
      - Comprehensively answered more than 5 business questions such as trends of the tweets, frequency of the words in each sentiment class etc.
      - Built machine learning model and achieved an accuracy of 80%.
   
   2. Toxic Comments Tweets:
      - Utilized deep learning techniques (LSTMs) for model creation and achieved a final accuracy of 99%.

## Screenshots Of The API
<img src="res/Snap1.png" width="400"/>    

<img src="res/Snap2.png" width="400"/>

<img src="res/Snap3.png" width="400"/>

## Steps Taken In This Project
- Data Collection
- EDA & Visualization
- Model selection & building it.
- Evaluation of the models.
- Saving the models.
- Development of REST API.

## Installation And Usage
1. Installation
   - Download/clone this repository. Then open terminal (make sure you are in the project's directory).
   - Create a virtual environment using the command ````py -m venv yourVenvName```` and activate it using ````yourVenvName\Scripts\activate.bat````.
   - Then run the following command ````pip install -r requirements.txt````. With this, all the dependencies will be installed in your virtual environment. 
> **Note:** *If any dependency is missing or an error shows up, install it using ````pip install moduleName````*.

2. Usage
   - Open your project folder and go to the terminal and activate your virtual environment. Then type ````uvicorn src.app:app --reload```` and there it'll give you the
   localhost address. Open the link and then use any of below endpoints for predictions.
   - '/covid/yourText' -> this is for sentiment analysis of covid19 tweets.
   - '/toxiccomment/yourText' -> this is for predicting multiple labels of toxicity in a tweet or text.
