from langchain_community.document_loaders import PyPDFLoader

# this loader in langchain used to load content from PDF files and convert each page into a document object, but not great for scanned or complex format PDFs, for these use:
# scannedPdf/image pdf : unstructuredPDFLoader or AmazonTextractPDFLoader
# pdf with tables: PDFPlumberLoader
# need layout and image data: PyMuPDFLoader
# etc

loader = PyPDFLoader('Modern_Bharat_Essay.pdf')

docs = loader.load()

print(len(docs))

print(docs[0])
