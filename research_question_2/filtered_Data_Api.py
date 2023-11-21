#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

# Assuming your dataset is in a CSV file named 'your_dataset.csv'
# Adjust the file name accordingly.
dataset_path = 'C:\\Users\\akash\\Result.csv'


# Read the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Set of keywords to filter questions
keywords = ["API", "API CALL","API ECONOMY","API GATEWAY","API INTEGRATION","API KEYS","API LIFECYCLE","API Layer","API Portal","API Request","API Security","Apigee","APIsec","Application","Burp Suite","CI/CD","CRUD","Cache","Client","DDoS","DevOps","DevSecOps","Developer Portal","External APIs","Framework","GET Method","GraphQL","HTTP Methods","JSON","Logic Flaw","Microservices","OWASP","Parameters","REST","Red Teams","SDK","SDLC","SOAP","SQL Injection","Webhook","ZAP"]# Add your specific keywords here

# Function to check if any keyword is present in the sentence
def contains_keywords(sentence):
    # Handle the case where the input is not a string (e.g., if it's a float)
    if isinstance(sentence, str):
        return any(keyword in sentence for keyword in keywords)
    else:
        return False

# Filter rows with questions based on the keywords
questions_df = df[df['Prompt'].apply(contains_keywords)]

# Save the filtered questions to a new CSV file
output_csv_path = 'filtered_questions.csv'
questions_df.to_csv(output_csv_path, index=False)

print(f"Filtered questions saved to {output_csv_path}")

