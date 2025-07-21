# LangChain Document Loaders Examples

This repository contains examples of different document loaders implemented using LangChain. These loaders help in processing various file formats for use in language models and other AI applications.

## Available Loaders

### 1. CSV Loader

The CSV loader provides two main approaches for loading CSV files:

#### Basic Row-by-Row Loading

```python
from langchain_community.document_loaders import CSVLoader

# Initialize loader
loader = CSVLoader("Social_Network_Ads.csv")

# Load documents
documents = loader.load()

# Access first document
print(documents[0])
```

#### Advanced Features

```python
# Load with specific columns and metadata
loader = CSVLoader(
    "Social_Network_Ads.csv",
    content_columns=["Gender", "Age", "EstimatedSalary"],
    metadata_columns=["User ID", "Purchased"],
    combine_columns=True,
    column_separator=" | "
)
```

### 2. PDF Loader

The PDF loader can extract text content from PDF files:

```python
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("dl-curriculum.pdf")
pages = loader.load()

# Access content from first page
print(pages[0].page_content)
```

### 3. Text File Loader

For simple text files:

```python
from langchain_community.document_loaders import TextLoader

# Load text file
loader = TextLoader("cricket.txt")
documents = loader.load()
print(documents[0].page_content)
```

### 4. Web Page Loader

For loading content from web pages:

```python
from langchain_community.document_loaders import WebBaseLoader

# Load web content
loader = WebBaseLoader("https://example.com")
documents = loader.load()
print(documents[0].page_content)
```

### 5. Directory Loader

For loading multiple files from a directory:

```python
from langchain_community.document_loaders import DirectoryLoader

# Load all text files from a directory
loader = DirectoryLoader("./books/", glob="**/*.txt")
documents = loader.load()
```

## Document Structure

Each loader returns documents in a standard format with:

- `page_content`: The main text content
- `metadata`: Additional information like source file, page numbers, etc.

Example document structure:

```python
Document(
    page_content="...",
    metadata={
        "source": "file.csv",
        "row": 0,
        "column": "text"
    }
)
```

## Features Across Loaders

1. **Metadata Handling**: All loaders preserve source information in metadata
2. **Content Processing**: Options to filter, combine, or transform content
3. **Lazy Loading**: Support for handling large files efficiently
4. **Error Handling**: Robust error handling for corrupt or invalid files

## Best Practices

1. Always check the content of the first few documents to verify correct loading
2. Use appropriate encoding settings when dealing with non-ASCII text
3. Consider memory usage with large files - use lazy loading when possible
4. Include error handling in production code
5. Validate the structure of input files before processing

## Dependencies

- langchain
- langchain-community
- pandas (for CSV processing)
- PyPDF2 (for PDF processing)
- beautifulsoup4 (for web content)
- chardet (for encoding detection)

## Installation

```bash
pip install langchain langchain-community pandas PyPDF2 beautifulsoup4 chardet
```
