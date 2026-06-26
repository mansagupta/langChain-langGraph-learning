from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
some python code"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])