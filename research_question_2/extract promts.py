#!/usr/bin/env python
# coding: utf-8

# In[32]:


import json
import pandas as pd


# In[ ]:





# In[34]:


with open(r'C:\Users\akash\Downloads\20230803_094705_issue_sharings.json') as fp:
    data = json.load(fp)


# In[35]:


data


# In[36]:


type(data)


# In[ ]:





# In[39]:


l1=[]
l2=[]
for source in data["Sources"]:
    chatgpt_sharing_entries = source.get("ChatgptSharing", [])
    for entry in chatgpt_sharing_entries:
        # Iterate over Conversations
        for conversation in entry.get("Conversations", []):
            prompt = conversation.get("Prompt", "")
            answer = conversation.get("Answer", "")
            
            l1.append(prompt)
            l2.append(answer)


# In[40]:


com_list  = list(zip(l1, l2))

df = pd.DataFrame(com_list, columns = ['Prompt', 'Answer'])
df


# In[41]:


df=df[df['Prompt'].map(lambda x: x.isascii())]


# In[48]:


df=df.reset_index(drop=True)


# In[50]:


df.to_csv("Result.csv")


# In[ ]:




