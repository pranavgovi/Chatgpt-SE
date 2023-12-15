#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load your CSV file into a Pandas DataFrame
df = pd.read_csv('filtered_questions.csv')

# Splited the dataset into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Created a pipeline with a TF-IDF vectorizer and a LinearSVC classifier
model = make_pipeline(TfidfVectorizer(), LinearSVC())

# Trained the model on the training data
model.fit(train_data['Prompt'], train_data['Answer'])

# Made predictions on the test data
predictions = model.predict(test_data['Prompt'])

# Saved the model for future use
joblib.dump(model, 'api_response_model.joblib')

# Used the trained model to generate a response for a new prompt
new_prompt = ["How do I authenticate with an API?"]
new_response = model.predict(new_prompt)
print(f"New Response: {new_response}")


# In[ ]:




