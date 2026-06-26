from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

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

parser = JsonOutputParser()  # this parse the output into JSON but is not able to enforce schema of your choice.

template = PromptTemplate(
    template= 'Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables= [],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.format()

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)