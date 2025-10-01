from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms.openai import OpenAI
import pandas as pd
from langchain.chat_models import ChatOpenAI

def query_agent(data,query):
	df = pd.read_csv(data)
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)	
	agent = create_pandas_dataframe_agent(llm,df,verbose=True, allow_dangerous_code=True)
	return agent.run(query)
