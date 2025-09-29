import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
my_access_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
print(my_access_token)

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

pipe = pipeline(
    "text2text-generation",
    model = "google/flan-t5-large",
    temperature=0.2
)

llm = HuggingFacePipeline(pipeline=pipe)
print(llm("what is currency of India"))
