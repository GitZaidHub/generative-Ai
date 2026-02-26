from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
documents = [
    "Virat Kohli is an Indian cricketer and captain of the Indian cricket team.",
    "Sachin Tendulkar is a former Indian cricketer and former captain.",
    "MS Dhoni is a former Indian cricketer and former captain.",
    "Rohit Sharma is an Indian cricketer and vice-captain.",
    "Javagal Srinath is a former Indian fast bowler."
]
query = "tell me about  indian fast bowler"
vectors = embeddings.embed_documents(documents) # documents -> vectors (embeddings)
vector = embeddings.embed_query(query) # query -> vector (embedding)
scores = (cosine_similarity([vector], vectors)[0]) # cosine similarity between query vector and document vectors
index , score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] #  index of the most similar document and its score
print(query)
print(f"Most similar document: {documents[index]} with score: {score}")

#*************************************** Summary of the File:******************************************
#******Imports and Setup:*******

# It imports GoogleGenerativeAIEmbeddings from langchain_google_genai to generate embeddings for text.
# It uses cosine_similarity from sklearn.metrics.pairwise to calculate the similarity between vectors.
# The dotenv library is used to load environment variables.

# *******Embedding Generation:********

# A GoogleGenerativeAIEmbeddings object is instantiated with the model gemini-embedding-001.
# A list of documents (about Indian cricketers) is defined.
# A query string, "tell me about indian fast bowler," is provided.

# ******Similarity Calculation:*********

# The documents are converted into embeddings (vectors) using embed_documents.
# The query is converted into an embedding using embed_query.
# Cosine similarity is calculated between the query vector and the document vectors.
# The document with the highest similarity score is identified and printed along with the score.

# *******Output:************

# The query is printed.
# The most similar document and its similarity score are displayed.

#******* Semantic Search:********

# Semantic search refers to the process of retrieving information based on the meaning and context of the query rather than exact keyword matches. In this file:

# Embeddings: The GoogleGenerativeAIEmbeddings model generates dense vector representations of the documents and query, capturing their semantic meaning.
# Cosine Similarity: Measures the similarity between the query vector and document vectors to find the most contextually relevant document.
# This approach enables the system to understand the intent behind the query and retrieve the most semantically relevant document.