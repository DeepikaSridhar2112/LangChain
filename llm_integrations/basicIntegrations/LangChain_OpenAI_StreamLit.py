import streamlit as st
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


def generateResponse(query):
    # Initialize the OpenAI model
    chat = ChatOpenAI(
    model="gpt-3.5-turbo",  
    temperature=0.7, 
    )
    response = chat([HumanMessage(content=query)])
    return response.content
def getQuery():
    input_text = st.text_input("Query: ", key="input")
    return input_text



st.set_page_config(page_title="HuggingFace LangChain Integration", page_icon=":robot:")
st.header("Chat")


load_dotenv(find_dotenv(), override=True)
mykey = os.getenv('OPENAI_API_KEY')

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

query=getQuery()
submit = st.button('Click me')

if submit:
    response = generateResponse(query)
    st.subheader("Answer:")
    st.write(response)
