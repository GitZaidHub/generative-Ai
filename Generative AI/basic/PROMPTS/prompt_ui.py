from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="models/gemini-flash-latest")

st.header("Research Assistant")


paper_input = st.selectbox("Select a paper", ["Attention is All You Need", "BERT: Pre-training of "
"Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select a style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select a length", ["Short (1-2 sentences)", "Medium (1-2 paragraphs)", "Long (1-2 pages)"])

#template
template = PromptTemplate(
    template=""" 
Please summarize the paper tiitled {paper_input} with the following Specifications:
Explanation Style: {style_input}
    Summary Length: {length_input}
    1. Mathematical Notation: Use mathematical notation where appropriate to explain concepts clearly and concisely.
    2. Code Snippets: Include code snippets in Python to illustrate key algorithms, models, or techniques discussed in the paper.
    3. Visual Aids: Incorporate visual aids such as diagrams, charts, or tables to enhance understanding and provide a visual representation of complex ideas.
    4. Examples: Provide concrete examples to demonstrate the application of concepts and techniques from the paper.
    5. Clarity and Conciseness: Ensure that the summary is clear, concise
""",
input_variables=["paper_input", "style_input", "length_input"]
)

# fill the template
prompt = template.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input})


if st.button("Summarize"):
    result = model.invoke(prompt)

    text = ""
    for block in result.content:
        if block.get("type") == "text":
            text += block["text"]

    st.write(text)
