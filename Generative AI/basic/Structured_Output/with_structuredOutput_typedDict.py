# from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional , Literal
from pydantic import Field , BaseModel

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id ="meta-llama/Llama-3.2-1B-Instruct",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm=llm)
model = ChatGoogleGenerativeAI(model="models/gemini-flash-latest")


#schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="The main themes or topics discussed in the review")
    summary : list[str] = Field(description="A concise summary of the review's content")
    sentiment:Literal["positive", "negative", "neutral"] = Field(description="The overall sentiment of the review, e.g., positive, negative, neutral")
    pros: Optional[list[str]] = Field(default=None,description="The positive aspects mentioned in the review, if any")
    cons: Optional[list[str]] = Field(default=None,description="The negative aspects mentioned in the review, if any")
    name: Optional[str] = Field(default=None,description="The name of the reviewer, if mentioned in the review")
    
structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""The smartwatch is a modern gadget designed to make daily life more convenient and efficient. It has a sleek and lightweight design, making it comfortable to wear all day. The display is bright and clear, allowing users to check time, notifications, and fitness data easily.

One of the main advantages of a smartwatch is its health-tracking features. It can monitor steps, heart rate, sleep patterns, and calories burned, which is very helpful for fitness-conscious users. The watch also connects smoothly with smartphones, enabling users to receive calls, messages, and app alerts directly on their wrist.

The battery life is decent and usually lasts one to two days with regular use. Overall, the smartwatch is a useful gadget that combines style, technology, and health features, making it suitable for students and working professionals.
Review by: Mohammad Zaid
""")

print(result)