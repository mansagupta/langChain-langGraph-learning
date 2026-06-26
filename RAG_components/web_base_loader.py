# this loader is used to load and extract text content from web pages(URLs), uses BeautifulSoup under the hood to parse HTML, loads only static content, use to parse blogs, news article or public websites, but does not handle JavaScript heavy pages use SeleniumURLLoader for that

from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.w3schools.com/python/python_generators.asp'

loader = WebBaseLoader(url) # can also pass list of URLs, it will generate one document object for every URL

docs = loader.load()

print(len(docs))

print(docs[0].page_content)