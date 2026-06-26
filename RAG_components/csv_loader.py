from langchain_community.document_loaders import CSVLoader

# creates a document object for every row present 
loader = CSVLoader(file_path='Social_Network_Ads.csv') 

data = loader.load()

print(len(data))
print(data[0])