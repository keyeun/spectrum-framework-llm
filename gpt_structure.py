import os
import openai
from tenacity import retry, stop_after_attempt, wait_fixed, wait_random_exponential
os.environ["OPENAI_API_KEY"] = 'Write Your Own Key'

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def gpt4o_json(system_prompt, user_prompt):
    completion = openai.chat.completions.create(
        model = 'gpt-4o',
        response_format = {'type': 'json_object'},
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
    )
    return completion.choices[0].message.content

def gpt3_json(system_prompt, user_prompt):
    completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        response_format = {'type': 'json_object'},
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
    )
    return completion.choices[0].message.content