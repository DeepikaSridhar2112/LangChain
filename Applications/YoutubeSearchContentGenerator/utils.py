from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, prompt
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun

def generate_script(user_prompt,video_length,creativity_limit,api_key):
	title_template = PromptTemplate(
		input_variables=['subject'],
	    template = 'Please come up with a title for Youtube vide on the subject - {subject}' )
	script_template=PromptTemplate(
		input_variable=['title','search_data','duration'],
		template='Create a script for Youtube video for the subject {title} for {duration} minutes using search engine {search_data}')
	llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature= creativity_limit, openai_api_key= api_key)
	title_chain= LLMChain(llm=llm, prompt=title_template, verbose=True)
	script_chain= LLMChain(llm=llm, prompt=script_template, verbose=True)

	search = DuckDuckGoSearchRun()
	title= title_chain.run(user_prompt)
	search_result = search.run(user_prompt)
	script = script_chain.run(title = user_prompt,search_data=search_result,duration=video_length)
	return search_result, script,title

