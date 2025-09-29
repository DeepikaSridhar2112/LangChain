import os
from dotenv import find_dotenv,load_dotenv

load_dotenv(find_dotenv(),override=True)
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-3.5-turbo",  
    temperature=0.7, 
)
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
response_schemas= [
    ResponseSchema(name="currency", description="Answer the query for the user"),
    ResponseSchema(name="abbreviation", description="Whats the abbreviation for the currency")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
print(output_parser)
format_instructions=output_parser.get_format_instructions()
print(format_instructions)
prompt_template = PromptTemplate(
    template="Answer as accurately as possible\n{format_instructions}\n{query}",
    input_variables=["query"],
    partial_variables = {"format_instructions" : format_instructions}
)
print(prompt_template)
prompt = prompt_template.format(query="Whats the currency of India")
output= chat.invoke([HumanMessage(content=prompt)])
print(output.content)
