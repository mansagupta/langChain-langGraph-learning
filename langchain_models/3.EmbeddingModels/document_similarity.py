from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions= 300)

documents = [
    "Narendra Modi is the longest serving Prime Minister of India",
    "I am going to bed before either of you come up with another clever idea of get us killed or worse EXPELLED!",
    "My receipts be looking like phone numbers, if it aint money then wrong number"
    "Channa mereya mereya channa mereya meraya channa mereya mereya beliya ohh piyaaaa...."
]

query = "tell me about Narendra Modi"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0] # both parameter should be 2D list and *[0] to covert the result into a single list

index , score = sorted(list(enumerate(score)),key = lambda x:x[1])[-1] # enumerate add extra column of index number and here we are sorting accoring to the score that why lambda is used and then we extracted the highest value byt doing [-1]

print(documents[index])
print("Similarity score is : ", score)



