#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
nltk.download('punkt')

# Import dataset 
data = pd.read_csv(r'C:\\Users\\akash\\filtered_questions.csv') 

# Get the text column
text = data['Prompt']

# Tokenization
tokenized_text = []
for sentence in text:
    tokens = word_tokenize(sentence) 
    tokenized_text.append(tokens)

# Stemming
ps = PorterStemmer()  
stemmed_text = []
for sentence in tokenized_text:
    stemmed_sentence = [ps.stem(word) for word in sentence]
    stemmed_text.append(stemmed_sentence)
    
print(stemmed_text)


# In[ ]:




