from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the famous for Hawra Bridge",
    "Ptna is the capital of Bihar"
]

result = embedding.embed_documents(documents)

print(str(result))