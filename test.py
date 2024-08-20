from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

AI_KEY = os.getenv('AI_KEY')




def generate_response(user_message):
    aiclient = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=
        AI_KEY
    )

    try:
        completion = aiclient.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=[{
                "role": "user",
                "content": user_message
            }],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=False 
        )

        response_text = completion.choices[0].message.content

        return response_text

    

    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred during the generation."

