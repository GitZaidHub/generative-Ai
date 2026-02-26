from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os # optional 
os.environ['HF_HOME']="G:/CodeKit/cache" # Set the cache directory for Hugging Face models
llm = HuggingFacePipeline.from_model_id(
    model_id = "meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(max_length=512, temperature=0.7)
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("Future of GenAi in jobs field?")
print(result.content)