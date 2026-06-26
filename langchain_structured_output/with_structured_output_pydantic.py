from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

# Typed dictionary is for presentation purpose only not data type validation.

load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel):
    summary: str
    sentiment: str

class Review2(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description= "A brief summary of the review")
    sentiment: Literal["POS", "NEG"] = Field(description="Return sentiment of the review either neagtive, positive or neutral")
    pros:Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description= "Write down all the cons inside a list")


structured_model = model.with_structured_output(Review2)

result = structured_model.invoke("The hardware is great, but the software feels blosted. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print(result)
print(result.summary)
print(result.sentiment)