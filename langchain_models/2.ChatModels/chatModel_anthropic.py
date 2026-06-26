from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3-5-sonnet-24241922')

result = model.invoke("what is the capital of India?")

print(result.content)