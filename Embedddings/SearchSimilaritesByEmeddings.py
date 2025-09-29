import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv(find_dotenv(),override=True)


st.set_page_config(page_title="similarties", page_icon=":rocket:")
st.header("Ask me and I will suggest similar thgs")

embeddings = OpenAIEmbeddings()

from langchain_community.document_loaders import TextLoader
loader  = TextLoader(file_path='data.txt')

from langchain_core.documents import Document

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

documents = [Document(page_content=line) for line in lines]

print(documents)
db = FAISS.from_documents(documents,embeddings)


def get_input():
    user_input = st.text_input("You: ",key= input)
    return user_input

user_input = get_input()
submit = st.button('Find Similar Things')

if submit:
   docs = db.similarity_search(user_input)
   st.subheader("Top Matches:")
   st.text(docs[0].page_content)
   st.text(docs[1].page_content)






