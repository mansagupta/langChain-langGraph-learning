from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1= ChatOpenAI()
model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate 5 short quedstion answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """An unnamed first-person narrator questions whether they can "do it," without disclosing what “it” refers to. The narrator introduces the titular character in the story, Salvatore. The narrator has known Salvatore since he was a young teen. He describes Salvatore during his adolescence as a good-natured, skinny young man who wasn't particularly attractive but didn't seem to care. Instead, he spent his days happily swimming, laughing, and enjoying being in nature. Although he had little to worry about in life, Salvatore did help to take care of his two younger brothers, who also loved to play outside and swim in the ocean. Their father was a hard-working fisherman, and their lifestyle was described as "frugal."

Salvatore grows up and falls in love with a beautiful girl from the Grande Marina, a busy fishing port on the island of Capri in Italy. They agree to marry, but the law requires Salvatore to serve in the military first. He enlists and leaves the island for the first time in his life to serve in the navy, crying as he departs because he so loves his home. On his trip, Salvatore realizes that his home landscape feels like a part of his body. He misses his fiancée most, and he writes to her regularly to profess his undying love as he travels to several areas of Italy and then to China where he becomes sick. Salvatore spends months in a Chinese hospital before being discharged from the service because he has developed a permanent illness. Salvatore receives the news happily, ignoring the fact that he has contracted a life-long disease, too excited that he will soon be returning home to his family and fiancée."""

result = chain.invoke({'text': text})

print(result)