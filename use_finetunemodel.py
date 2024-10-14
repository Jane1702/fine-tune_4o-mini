from openai import OpenAI 
import os
client = OpenAI()
os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::AIE36qad",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me all information about Trang who is apprentice at Eviden"}
  ]
)

print(completion.choices[0].message)