import os
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",   
)

prompt = PromptTemplate(
    template = 'Write a summary for the following poem -\n{poem}',
    input_variables=["poem"],)


loader = TextLoader("cricket.txt", encoding="utf-8")
os.system('clear')
documents = loader.load()

# print(documents[0])

# print(type(documents))
# print(len(documents))
# print(type(documents[0]))


chain = prompt | model | parser
result  = chain.invoke({"poem": documents[0].page_content})
print(result)