# Using free api of hugging face

# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_community.llms import HuggingFaceHub
# from dotenv import load_dotenv

# load_dotenv()

# # Step 1: Load Hugging Face model
# llm = HuggingFaceHub(
#     repo_id="google/flan-t5-base",   # simple free model
#     model_kwargs={"temperature": 0.5, "max_length": 100}
# )

# # Step 2: Create Prompt Template
# prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Explain {topic} in simple terms for beginners."
# )

# # Step 3: Create Chain
# chain = LLMChain(llm=llm, prompt=prompt)

# # Step 4: Run Chain
# output = chain.run("machine learning")

# print(output)



# Using openai api

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 intresting fact about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)