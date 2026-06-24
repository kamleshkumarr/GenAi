from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

document = [
    "Virat kohli is an Indian cricketer known for his aggressive batting and leadership",
    "Ms Dhoni is a former Indian captain famous for his calm demeaner and finishing sills",
    "Sachin Tendulkar, also known as the 'God of cricket', hold many batting records",
    "Rohit Sharma is known for his elegant batting and records-breaking doble centuries"
]

query = 'tell me about virat kohli'

doc_embedding = embedding.embed_documents(document)

query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding], doc_embedding))