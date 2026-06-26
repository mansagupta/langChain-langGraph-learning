print("Starting...")

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

print("Loading model...")

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100        
    )
)

print("Model loaded")

model = ChatHuggingFace(llm=llm)

print("Invoking model...")

result = model.invoke("What is the capital of India?")

print("Result received")
print(result.content)