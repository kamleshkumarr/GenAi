from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

# 1st promt -> detailed report
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}'
    input_variables=['topic']
)


# 2nd Promt -> summary
template2 = PromptTemplate(
    template ='Write a line summary on following text. / {text}'
    input_variables=['text']
)

promt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(promt1)

promt2 = template2.invoke({'text': result.content})

result1 = model.invoke(promt2)

print(result1.content)


# Using String parser

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser  # Chaining

result = chain.invoke({'topic': 'black hole'})

print(result)