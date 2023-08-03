# import tflearn 
import string
import os
import nltk
import tensorflow as tf
import numpy as np
import pandas as pd
import json
import nltk.corpus
from scrapy.crawler import CrawlerProcess
from nltk.stem.lancaster import LancasterStemmer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, GlobalMaxPooling1D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow import keras
from nltk.util import pr
from nltk.corpus import stopwords
from textblob import TextBlob
from fuzzywuzzy import fuzz

nltk.download('stopwords')
df = pd.read_csv ('training_data_set_final.csv')
df['input'] = df['input'].apply(lambda wrd:[ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])
df['input'] = df['input'].apply(lambda wrd: ''.join(wrd))
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(df['input'])
train = tokenizer.texts_to_sequences(df['input'])
x_train = pad_sequences(train)
le = LabelEncoder()
y_train = le.fit_transform(df['tag'])
input_shape = x_train.shape[1]  
model = keras.models.load_model('saved_model.h5')
def debate(user_response,data):
        data = json.loads(data)
        texts_p = []
        user_response = [letters.lower() for letters in user_response if letters not in string.punctuation]
        user_response = ''.join(user_response)
        texts_p.append(user_response)
        user_response = tokenizer.texts_to_sequences(texts_p)
        user_response = np.array(user_response).reshape(-1)
        user_response = pad_sequences([user_response], input_shape)
        output = model.predict(user_response)
        output = output.argmax()
        response_tag = le.inverse_transform([output])[0]
        if (response_tag == "pros"):
                f = data["cons"]
        if (response_tag == "cons"):
                f = data["pro"]
        if (response_tag == "neutral"):
                f = data["neutral"]
        best_match = None
        best_score = -1

        for line in f:
                line = line.strip()
                similarity_score = fuzz.token_set_ratio(line, user_response)
                if similarity_score > best_score:
                        best_score = similarity_score
                        best_match = line
        return best_match
