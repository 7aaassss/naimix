from openai import OpenAI

client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key="secret"
)


def get_llm_answer(system_prompt, mes, client=client):
    messages = [
        {"role": "system", "content": system_prompt,
            
        "role": "user", "content": mes}
    ]
    
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct", 
        messages=messages, 
        temperature=0.9,
        n=1
    )
    
    return completion.choices[0].message.content

def preproc_info(text):
    return str(get_llm_answer)
    
res = get_llm_answer