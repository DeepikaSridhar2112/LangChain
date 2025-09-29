import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
import pandas as pd
df= pd.read_csv('embeddings_data.txt')
df['embedding'] = df['Words'].apply(lambda x: embeddings.embed_query(x))
df.to_csv('embeddings_with_words.txt')

df_with_embeddings = pd.read_csv('embeddings_with_words.txt')
print(df_with_embeddings['embedding'])
my_input = "mango"
text_embeddings = embeddings.embed_query(my_input)
print(text_embeddings)
import numpy as np

def cosine_similarity(a, b):
    a=a.replace('[','')
    a=a.replace(']','')
    a = list(map(float, a.split(',')))
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
df_with_embeddings['similarity_score'] = df_with_embeddings['embedding'].apply(lambda x: cosine_similarity(x, text_embeddings))
print(df_with_embeddings['similarity_score'])
df_with_embeddings.sort_values('similarity_score', ascending=False)
print(df_with_embeddings['similarity_score'])

