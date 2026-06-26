# chunk size is defined in this on the basis of characters or tokens.

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Modern_Bharat_Essay.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

text = """An unnamed first-person narrator questions whether they can "do it," without disclosing what “it” refers to. The narrator introduces the titular character in the story, Salvatore. The narrator has known Salvatore since he was a young teen. He describes Salvatore during his adolescence as a good-natured, skinny young man who wasn't particularly attractive but didn't seem to care. Instead, he spent his days happily swimming, laughing, and enjoying being in nature. Although he had little to worry about in life, Salvatore did help to take care of his two younger brothers, who also loved to play outside and swim in the ocean. Their father was a hard-working fisherman, and their lifestyle was described as "frugal." """

result = splitter.split_text(text)
result2 = splitter.split_documents(docs)

print(result2)