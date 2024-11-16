import os
from dotenv import load_dotenv
import json
from openai import OpenAI
from preproc import Processor

class SVMAnalyzer:
    def __init__(self, system_prompt_file="./system_prompt.txt"):
        """
        Initializes the SVMAnalyzer with the system prompt and OpenAI client.
        """
        load_dotenv()
        api_key = os.getenv("HF_API_KEY")
        if api_key is None:
            raise ValueError("API key not found in environment variables.")

        self.client = OpenAI(
            base_url="https://api-inference.huggingface.co/v1/",
            api_key=api_key
        )

        with open(system_prompt_file, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def get_llm_answer(self, message):
        """
        Sends a message to the LLM and returns the response.
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": message}
        ]

        completion = self.client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=messages,
            temperature=0.9,
            n=1,
            max_tokens=1500,
        )

        return completion.choices[0].message.content

    def get_processed_data(self,text1, text2):
        """
        Processes two files using the Processor class and returns the results as two strings.
        """
        processor1 = Processor(text1, before=2, after=0)
        contexts1 = processor1.extract_work_related_contexts()
        result1 = "\n\n".join(["--- Контекст ---\n" + "\n".join(context) for context in contexts1])

        processor2 = Processor(text2, before=0, after=2)
        contexts2 = processor2.extract_work_related_contexts()
        result2 = "\n\n".join(["--- Контекст ---\n" + "\n".join(context) for context in contexts2])

        return result1, result2

    def predict_svm(self, text1, text2, fp_grade, sp_grade):
        """
        Main function to process data and call the LLM.
        """
        fp_description, sp_description = self.get_processed_data(text1, text2)

        message = f"{{fp_grade : {fp_grade}, fp_description: {fp_description}, sp_grade = {sp_grade}, sp_description: {sp_description}}}"

        llm_response = self.get_llm_answer(message)

        return llm_response

        # If you need to parse the JSON response (as commented out in your original code):
        # try:
        #     json_response = json.loads(llm_response)
        #     return json.dumps(json_response, indent=4)
        # except json.JSONDecodeError as e:
        #     print(f"JSON decoding error: {e}")
        #     print("LLM response:\n", llm_response)
        #     return llm_response  # Or handle the error as needed