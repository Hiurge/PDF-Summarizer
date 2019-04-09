from bs4 import BeautifulSoup
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Set stop words
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['RT', 'rt'])

# Initiate sub-parts
WNL = WordNetLemmatizer()

def remove_mentions(text):
    return ' '.join([w for w in text.split(' ') if not w.startswith('@')])
def remove_url(text):
    return re.sub('https?://[A-Za-z0-9./]+','',text)
def html_strip_lxml(text):
    return BeautifulSoup(text, 'lxml').get_text()
def remove_special_characters(text):
    return re.sub("[^a-zA-Z]", " ", text)
def lowercase_text(text):
    return text.lower()
def strip_inner_spaces(text):
    return ' '.join([w.strip() for w in text.split()])
def remove_stop_words(text):
    return ' '.join([w for w in text.split() if not w in set(stopwords)])
def lemmatize_words(text, WNL):
    return ' '.join([WNL.lemmatize(word, pos='v') for word in text.split()])
# TEXT CLEANER

from bs4 import BeautifulSoup
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Set stop words
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['RT', 'rt'])

# Initiate sub-parts
WNL = WordNetLemmatizer()

def remove_mentions(text):
    return ' '.join([w for w in text.split(' ') if not w.startswith('@')])
def remove_url(text):
    return re.sub('https?://[A-Za-z0-9./]+','',text)
def html_strip_lxml(text):
    return BeautifulSoup(text, 'lxml').get_text()
def remove_special_characters(text, preserve):
    return re.sub("[^a-zA-Z{}]".format(preserve), " ", text)
def lowercase_text(text):
    return text.lower()
def strip_inner_spaces(text):
    return ' '.join([w.strip() for w in text.split()])
def remove_stop_words(text):
    return ' '.join([w for w in text.split() if not w in set(stopwords)])
def lemmatize_words(text, WNL):
    return ' '.join([WNL.lemmatize(word, pos='v') for word in text.split()])

def cleaner(text):
    text = remove_mentions(text)
    text = remove_url(text)
    text = html_strip_lxml(text)
    text = remove_special_characters(text,preserve='.')
    text = lowercase_text(text)
    text = strip_inner_spaces(text)
    text = remove_stop_words(text)
    #text = lemmatize_words(text, WNL)
    return text

def sentence_tokenizer_cleaner(text):
    text = remove_url(text)
    text = html_strip_lxml(text)
    #text = remove_special_characters(text,preserve='.!?')
    text = strip_inner_spaces(text)
    return text

def custom_cleaner(text):
    text = remove_url(text) # Dont use for link catch-up
    text = html_strip_lxml(text) # Dont use to split layout paragraphs
    text = remove_special_characters(text, preserve='') #='.?!') #234567890') # Dont use for dates
    text = lowercase_text(text) # Dont for entities
    text = strip_inner_spaces(text)
    text = remove_stop_words(text)
    #text = lemmatize_words(text, WNL)
    return text

def BOW_cleaner(text):
    text = remove_url(text) # Dont use for link catch-up
    text = html_strip_lxml(text) # Dont use to split layout paragraphs
    text = remove_special_characters(text, preserve='') #='.?!') #234567890') # Dont use for dates
    text = lowercase_text(text) # Dont for entities
    text = strip_inner_spaces(text)
    text = remove_stop_words(text)
    text = lemmatize_words(text, WNL)
    return text

def EXPLORATION_cleaner(text):
    text = remove_url(text) # Dont use for link catch-up
    text = html_strip_lxml(text) # Dont use to split layout paragraphs
    text = remove_special_characters(text, preserve='') #='.?!') #234567890') # Dont use for dates
    text = lowercase_text(text) # Dont for entities
    text = strip_inner_spaces(text)
    text = remove_stop_words(text)
    #text = lemmatize_words(text, WNL)
    return text

def TO_SUMMARY_cleaner(text):
    text = remove_url(text) # Dont use for link catch-up
    text = html_strip_lxml(text) # Dont use to split layout paragraphs
    text = remove_special_characters(text, preserve='') #='.?!') #234567890') # Dont use for dates
    text = lowercase_text(text) # Dont for entities
    text = strip_inner_spaces(text)
    text = remove_stop_words(text)
    #text = lemmatize_words(text, WNL)
    return text

# Usage single
#clean = cleaner('your text')

# Usage dataframe
#df['clean_COLUMN_NAME'] = df.COLUMN_NAME.apply(cleaner)


# Usage
# -----

# Usage single
#clean = cleaner('your text')

# Usage dataframe
#df['clean_COLUMN_NAME'] = df.COLUMN_NAME.apply(cleaner)


# Testing
# -------

# def test_single_text():
#     text = 'A random words flowing through my mind rig4h38t now.'
#     clean = cleaner(text)
#     print('>', text)
#     print('>', clean)

# def test_whole_dataframe():
#     import pandas as pd
#     import requests
#     import io

#     url = 'https://raw.githubusercontent.com/t-davidson/hate-speech-and-offensive-language/master/data/labeled_data.csv'
#     content = requests.get(url).content
#     df = pd.read_csv(io.StringIO(content.decode('utf-8'))).iloc[:,1:]

#     df['clean_tweet'] = df.tweet.apply(cleaner)

#     print('>', df['tweet'][7])
#     print('>', df['clean_tweet'][7])

#test_single_text()
#test_whole_dataframe()