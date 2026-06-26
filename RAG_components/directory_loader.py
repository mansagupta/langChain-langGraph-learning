from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books', # folder path
    glob = '*.pdf', # means load all pdf files from the folder
    loader_cls= PyPDFLoader
)

docs = loader.load() # loads everything at once in the memory, returns a list of document object, best when number of docs are small

docs1 = loader.lazy_load() # loads on demand, documents are fetched at a time as needed, returns generator of document objects, best when number of documents are large

print(len(docs))