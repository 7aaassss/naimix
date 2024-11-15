import os
from dotenv import load_dotenv
import json
from openai import OpenAI
from preproc import Processor

with open("./system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

load_dotenv()

api_key = os.getenv("HF_API_KEY")

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
        n=1,
        max_tokens= 1500,
        )
    
    return completion.choices[0].message.content

def get_proccessed_data(file_path_1, file_path_2):
    """
    Обрабатывает два файла с помощью класса Processor и возвращает результаты в виде двух строк.

    Args:
        file_path_1: Путь к первому файлу.
        file_path_2: Путь к второму файлу.

    Returns:
        Кортеж из двух строк: результат обработки первого файла и результат обработки второго файла.
    """

    processor1 = Processor(file_path_1, before =2, after = 0)
    contexts1 = processor1.extract_work_related_contexts()
    result1 = "\n\n".join(["--- Контекст ---\n" + "\n".join(context) for context in contexts1])

    processor2 = Processor(file_path_2,before=0,after = 2)
    contexts2 = processor2.extract_work_related_contexts()
    result2 = "\n\n".join(["--- Контекст ---\n" + "\n".join(context) for context in contexts2])

    return result1, result2

def main(file_path_1, file_path_2, fp_grade, sp_grade):
    """
    Основная функция для обработки данных и вызова LLM.
    """
    fp_description, sp_description = get_proccessed_data(file_path_1, file_path_2)

    message = f"""{{fp_grade : {fp_grade}, fp_description: {fp_description}, sp_grade = {sp_grade}, sp_description: {sp_description}}}"""

    llm_response = get_llm_answer(system_prompt, message, client=client)

    return llm_response
    # try:
    #     json_response = json.loads(llm_response)
    #     print(json.dumps(json_response, indent=4))
    # except json.JSONDecodeError as e:
    #     print(f"Ошибка декодирования JSON: {e}")
    #     print("Ответ LLM:\n", llm_response) 


file_path_1 = "./base1.txt"
file_path_2 = ".//base2.txt"
fp_grade = "Software Engineer"
sp_grade = "Project Manager"

print(main(file_path_1, file_path_2, fp_grade, sp_grade))
