import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
mykey = os.getenv('OPENAI_API_KEY')
print(mykey)

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize the OpenAI model
chat = ChatOpenAI(
    model="gpt-3.5-turbo",  
    temperature=0.7, 
)

# Send a message to the model
response = chat([HumanMessage(content="What is currency of India")])

# Print the response
print(response.content)
