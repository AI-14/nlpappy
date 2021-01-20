import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation
import re, unicodedata


'''If any error from nltk is raised, run the following script

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
'''


def to_lowercase(text):
    return text.lower()


def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)


def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def remove_punctuation(text):
    PUNCT_TO_REMOVE = punctuation
    PUNCT_TO_REMOVE += '’'
    clean_txt = ''.join([ch for ch in text if ch not in PUNCT_TO_REMOVE])
    return clean_txt


def tokenize_text(text):
    return word_tokenize(text)


def remove_stop_words(text):
    STOP_WORDS = stopwords.words('english')
    new_words = []
    for word in text:
        if word not in STOP_WORDS:
            new_words.append(word)
    return new_words


def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    lem_list = [lemmatizer.lemmatize(word) for word in text]
    return lem_list


def clean_text(text):
    text = to_lowercase(text)
    text = remove_urls(text)
    text = remove_emoji(text)
    text = remove_punctuation(text)
    text = tokenize_text(text)
    text = remove_stop_words(text)
    text = remove_non_ascii(text)
    text = lemmatize_text(text)
    return text
