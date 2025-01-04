
import openai

model = "llama3.2"
openapi = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

chat = openapi.chat.completions.create(model=model, messages=[{"role": "user", "content": "Can you create me a list of dishes I can create based on vegetable I list?"}])
print(chat.choices[0].message.content)

user_input = input("Tomato, potato, lettuce, Brinjal, cardamom, chillies")

chat = openapi.chat.completions.create(model=model, messages=[{"role": "user", "content": user_input}])
print(chat.choices[0].message.content)