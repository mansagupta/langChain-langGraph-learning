from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=200
    )
)

model = ChatHuggingFace(llm = llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template= 'write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template= 'write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.content)