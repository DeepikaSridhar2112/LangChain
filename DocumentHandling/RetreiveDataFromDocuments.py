!pip install sentence-transformers
!pip install faiss-cpu
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

loader = TextLoader('sample.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
chunks= text_splitter.split_documents(documents)
print(chunks)
embeddings = SentenceTransformerEmbeddings(model_name = 'all-MiniLM-L6-v2')
data_store = FAISS.from_documents(chunks,embeddings)
print(data_store)
data_retriever = data_store.as_retriever(search_kwags={"k":1})
print(data_retriever)

docs = data_retriever.get_relevant_documents("How many states are there in India?")
print(docs)
docs = data_retriever.get_relevant_documents("Name any leader of India")
print(docs)
