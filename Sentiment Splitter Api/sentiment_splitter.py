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
def split(data):
        data = json.loads(data)
        dict = {
                "pro" : [] , 
                "cons" : [] ,
                "neutral" : []
        }
        for input_line  in data:
                print(input_line)
                texts_p = []
                prediction_input = input_line
                prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
                prediction_input = ''.join(prediction_input)
                texts_p.append(prediction_input)
                prediction_input = tokenizer.texts_to_sequences(texts_p)
                prediction_input = np.array(prediction_input).reshape(-1)
                prediction_input = pad_sequences([prediction_input], input_shape)
                output = model.predict(prediction_input,verbose = 0)
                output = output.argmax()
                response_tag = le.inverse_transform([output])[0]
                print(response_tag)
                if response_tag == 'pros':
                        dict['pro'].append(input_line)
                if response_tag == 'cons':
                        dict['cons'].append(input_line)
                if response_tag == 'neutral':
                        dict['neutral'].append(input_line)
        data = json.dumps(dict, indent = 8) 
        return data



