from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

input_text = "ai is changing the world why ?"

inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(inputs["input_ids"], max_length=50)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))