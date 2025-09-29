from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
llm = ChatOpenAI(model_name='gpt-3.5-turbo')

template = "Can you create a post for tweet in {wordcount} words for the following input: {user_input}"

prompt_template = PromptTemplate(
        input_variables=["user_input","wordcount"], 
        template=template
    )

word_count= input("Enter the number of words you need")
input_prompt = input("Enter a prompt for the LLM")
filled_prompt = prompt_template.format(wordcount=word_count,user_input=input_prompt)



messages = [
        HumanMessage(content=filled_prompt)
    ]

llm(messages)
