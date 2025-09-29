import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
input_text= "hey hello"
text_embedding = embeddings.embed_query(input_text)
print(text_embedding)
