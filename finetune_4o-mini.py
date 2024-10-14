from openai import OpenAI 
import os
client = OpenAI()
MODEL="gpt-4o-mini"
os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

vFile=client.files.create(
  file=open("data.jsonl", "rb"),
  purpose="fine-tune"
)
vJob=client.fine_tuning.jobs.create(
  training_file=vFile.id, 
  model="gpt-4o-mini-2024-07-18")



