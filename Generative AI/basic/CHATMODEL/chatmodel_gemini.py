from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="models/gemini-flash-latest",temperature=0.7)

result = model.invoke("What is Rag system?")
print(result.content)

