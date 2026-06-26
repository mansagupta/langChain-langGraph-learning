from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv

# this primitive runnable allows us to apply custom Python functions within the AI pipeline. it acts as a middleware b/w different AI components, enabling preprocessing, transformation, API calls, filtering and post-processing in a Langchain workflow

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x:len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)