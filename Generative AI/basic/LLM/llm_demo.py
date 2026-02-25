from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="models/gemini-flash-latest")
result = llm.invoke("define Rag System in simplest words?")

print(result)

# from google import genai

# client = genai.Client(
#     api_key="AIzaSyB1gn1El2HeA0tVADq0s5W47o6p54tAOdg"
# )

# response = client.models.generate_content(
#     model="models/gemini-flash-latest",
#     contents="Explain RAG in simple words"
# )

# print(response.text)