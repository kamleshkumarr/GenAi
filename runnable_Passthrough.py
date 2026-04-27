from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from huggingface_hub import InferenceClient
import os

load_dotenv()

# HF client
client = InferenceClient(api_key=os.environ["HF_TOKEN"])

# HF wrapper
def hf_model(input_data):
    # 🔥 Convert LangChain input to plain string
    if hasattr(input_data, "to_string"):
        text = input_data.to_string()
    else:
        text = str(input_data)

    completion = client.chat.completions.create(
        model="google/gemma-4-31B-it:novita",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": text}],
            }
        ],
    )
    return completion.choices[0].message.content   


hf_runnable = RunnableLambda(hf_model)
parser = StrOutputParser()

# Prompt 1: Joke
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_chain = prompt1 | hf_runnable | parser

# Prompt 2: Explanation
prompt2 = PromptTemplate(
    template='Explain the joke:\n{text}',
    input_variables=['text']
)

explanation_chain = prompt2 | hf_runnable | parser

# ✅ Final chain
final_chain = (
    joke_chain
    | RunnableParallel({
        "joke": RunnablePassthrough(),
        "explanation": explanation_chain
    })
)

# run the final chain
result = final_chain.invoke({"topic": "cricket"})
print(result)