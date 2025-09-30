from sqlite3 import TimeFromTicks
from langchain.prompts import example_selector
import streamlit as st
from dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.prompts import PromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import streamlit as st

load_dotenv(find_dotenv(),override=True)
def generate_examples(age):
    if(age == "kid"):
            return [
             {
               "query": "What is a mobile" ,
                "answer":"Its a magical device which lets us see people"
             },
             {
                "query":"What happens when you get sick",
               "answer":"I love to sleep and drink my tonic"
             },
             {
                  "query":"Do you like your mom or dad",
                   "answer":"I love my mom like sun and dad like moon"
              },
              {
                    "query":"What do you want to become",
                      "answer":"I want to become an icecream man"
                 }
             ]
    if(age == "adult"):
                    return [
             {
               "query": "What is a mobile" ,
                "answer":"Its a device used for communication "
             },
             {
                "query":"What happens when you get sick",
               "answer":"I sleep well, recover and feel energetic"
             },
             {
                  "query":"Do you like your mom or dad",
                   "answer":"I love my family"
              },
              {
                    "query":"What do you want to become",
                      "answer":"I am already an engineer , I aim to become a lovable dad"
                 }
             ]
    if(age == "senior citizen"):
                    return [
             {
               "query": "What is a mobile" ,
                "answer":"I am too old to use mobile, i know about telephone"
             },
             {
                "query":"What happens when you get sick",
               "answer":"I am old, so i am always sick"
             },
             {
                  "query":"Do you like your mom or dad",
                   "answer":"I dont remember whom i used to like"
              },
              {
                    "query":"What do you want to become",
                      "answer":"In next birth i want to become a social worker"
                 }
             ]
def generate_response(age,task_type,user_query):
    examples= generate_examples(age)
    sample_template="""
     Question: {query},
     Response: {answer}
    """

    example_prompt = PromptTemplate(
     input_variables=["query","answer"],
     template=sample_template)

    prefix= """You are a {template_age} and {template_task_type}
        Here are some examples:
    """

    suffix = """
    Question: {userInput}
    Response:"""
    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200)
    prompt_template= FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt= example_prompt,
        prefix = prefix,
        suffix= suffix,
        input_variables=["userInput","template_age","template_task_type"],
        example_separator="\n")
    query= form_input
    human_message_prompt = HumanMessagePromptTemplate(prompt= prompt_template)
    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])

    prompt = chat_prompt.format_prompt(userInput=user_query,template_age=age,template_task_type=task_type)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

    messages = prompt.to_messages()
    for message in messages:
        print(message.content)


    output= llm.invoke(prompt)
    return output.content


st.set_page_config(page_title="Marketing Application",
                   page_icon= ":tick:",
                   layout= "centered",
                   initial_sidebar_state="collapsed")
st.header("How can I help you today")
form_input = st.text_area("Enter Text", height=275)
tasktype_option = st.selectbox('Please select the action to be performed',
                               ('Write a tweet','Write a sales copy','Write product description'),key=1)

age_option = st.selectbox('Relevant to which age group',('kid','adult','senior citizen'),key=2)
number_of_words = st.slider('Words Limit',1,200,25)
submit = st.button('Generate')
if submit:
    st.write(generate_response(age_option,tasktype_option,form_input))
