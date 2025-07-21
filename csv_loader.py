from langchain_community.document_loaders import CSVLoader
import os
os.system('clear')

loader = CSVLoader(file_path="Social_Network_Ads.csv")

data = loader.load()

print(len(data))  # Print the number of documents loaded
for doc in data:
    print(doc.page_content)  # Print the content of each document
    print("-----")  # Separator for clarity
# This code loads a CSV file using CSVLoader and prints the number of documents loaded along with their content.
# Ensure that the CSV file path is correct and accessible in your environment.