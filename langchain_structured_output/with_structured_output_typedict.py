from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

# Typed dictionary is for presentation purpose only not data type validation.

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):
    summary: str
    sentiment: str

class Review2(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, Optional[Literal["POS", "NEG"]], "Return sentiment of the review either neagtive, positive or neutral"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but the software feels blosted. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print(result)
print(result['summary'])
print(result['sentiment'])