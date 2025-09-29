from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import streamlit as st

def generate_response(query):
    st.session_state.sessionMessages.append(HumanMessage(content=query))
    chat = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature = 0.3
    )
    response = chat(st.session_state.sessionMessages)
    st.state.sessionMessages.append(AIMessage(content = response.context))
    return response.content

def get_inputs():
    user_input= st.text_input("Prompt: ", key= "input")
    return user_input

st.header("chatmodel")
st.set_page_config(page_title="chat-model-integration", page_icon=":rocket:")
if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are an assistant helping people")
    ]
    
user_input = get_inputs()
submit = st.button("Click me")

if submit:
    response = generate_response(user_input)
    st.subheader("Response:")
    st.write(response,key=1)
