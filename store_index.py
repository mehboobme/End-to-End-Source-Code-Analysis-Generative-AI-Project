from src.helper import repo_ingestion, load_repo, text_splitter, load_embedding
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
import os

load_dotenv()

OPEN_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPEN_API_KEY

# url = https://github.com/mehboobme/Medical_Chatbot.git"
#repo_ingestion(url)

documents = load_repo("repo/")
text_chunks = text_splitter(documents)
embeddings = load_embedding()

#storing vector in ChromaDB
vectorDB = Chroma.from_documents(text_chunks, embedding=embeddings, persist_directory='./db')
vectorDB.persist()
