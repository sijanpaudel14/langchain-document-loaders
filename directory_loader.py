import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.system('clear')
parser = StrOutputParser()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)
loader = DirectoryLoader(
    path = "books",
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)
# documents = loader.load()
# # print(f"Number of documents loaded: {len(documents)}")
# print(f"First document content: {documents[325].page_content}")  # Print first 500 characters of the first document
# print(f"Metadata of the first document: {documents[325].metadata}")

documents = loader.lazy_load()
for doc in documents:
    # print(f"Document content: {doc.page_content[:500]}")  # Print first 500 characters of each document
    print(f"Metadata: {doc.metadata}")
    print("-" * 80)  # Separator for clarity