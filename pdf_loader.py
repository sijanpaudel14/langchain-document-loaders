import os
from langchain_community.document_loaders import PyPDFLoader
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

loader = PyPDFLoader("dl-curriculum.pdf")
documents = loader.load()
print(f"Number of pages loaded: {len(documents)}")

print(documents[0].page_content)  # Print first 500 characters of the first page
print(documents[1].metadata)