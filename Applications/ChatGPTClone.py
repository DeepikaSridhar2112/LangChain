from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory,
												  ConversationSummaryMemory,
												  ConversationBufferWindowMemory)
import streamlit as st
from streamlit_chat import message

def get_response(user_input, api_key):
	if st.session_state['conversation'] is None:
		llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9, openai_api_key=api_key)
		st.session_state['conversation']  = ConversationChain(llm = llm,
												verbose = True,
												memory = ConversationBufferMemory())

	response = st.session_state['conversation'].predict(input = user_input)
	return response

if 'conversation' not in st.session_state:
	st.session_state['conversation'] = None
if 'messages' not in st.session_state:
	st.session_state['messages'] = []
if 'API_Key' not in st.session_state:
	st.session_state['API_key'] = ''
st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1> How can i assist you today </h1>", unsafe_allow_html=True)
st.sidebar.title(":smiley:")
st.session_state['API_key']=st.sidebar.text_input("Whats your API key?", type = "password")
summarise_button=st.sidebar.button("Summarise the conversation", key="summarise")

if summarise_button:
    summarise_placeholder= st.sidebar.write("Nice chatting with you my friend ♥: \n\n"+st.session_state['conversation'].memory.buffer)


response_container = st.container()
container = st.container()

with container:
	with st.form(key="my_form", clear_on_submit=True):
		user_input=st.text_area("Your question goes here:", key="input", height=100)
		submit = st.form_submit_button(label='send')
		if submit:
			api_key= st.session_state['API_key']
			st.session_state['messages'].append(user_input)
			model_response= get_response(user_input, api_key)
			st.session_state['messages'].append(model_response)
			with response_container:
				for i in range(len(st.session_state['messages'])):
					if i%2==0:
						message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
					else:
						message(st.session_state['messages'][i], key=str(i) + '_Ai')
