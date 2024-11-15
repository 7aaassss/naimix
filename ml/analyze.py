import os
from openai import OpenAI
from preproc import Preprocessor

api_key = os.environ.get("HF_API_KEY")

if api_key is None:
    raise ValueError("API key not found in environment variables.")

client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key=api_key  
)

def get_llm_answer(system_prompt, mes, client=client):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": mes}
    ]
    
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct", 
        messages=messages, 
        temperature=0.9,
        n=1
    )
    
    return completion.choices[0].message.content



