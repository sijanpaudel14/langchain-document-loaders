import os
from langchain_community.document_loaders import WebBaseLoader
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

prompt = PromptTemplate(
    input_variables=["question", 'text'],
    template = "Answer the following question \n {question} \n based on the following text: \n {text}",
)



url = "https://www.flipkart.com/ultimus-pro-intel-celeron-dual-core-n4020-4-gb-128-gb-emmc-storage-windows-11-home-nu14u4inc43bn-sg-thin-light-laptop/p/itme950115652bb0?pid=COMGY42B4VWGZZQ8&lid=LSTCOMGY42B4VWGZZQ8BZVWZU&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=4be1c396-9a95-48c4-a26d-a77abb21f156.COMGY42B4VWGZZQ8.SEARCH&ppt=pp&ppn=pp&ssid=yaom9lgcs00000001753097193005&qH=312f91285e048e09"  # Example URL, replace with your desired URL
loader = WebBaseLoader(url)

documents = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    "question": "What are the specifications of the laptop?",
    "text": documents[0].page_content
})

print(result)
print("Done")
# This code loads a webpage using WebBaseLoader, extracts the content, and uses a language model to answer a question based on that content.
