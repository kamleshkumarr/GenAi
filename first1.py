from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt =  'Moral of the thirsty crow'

result = generator(prompt, max_length=50)

print(result[0])

