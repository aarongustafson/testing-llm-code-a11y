import openai
import time
import json
import os
import uuid
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up your Azure OpenAI API key and endpoint
openai.api_key = os.getenv('AZURE_OPENAI_API_KEY')
openai.api_base = os.getenv('AZURE_OPENAI_API_BASE')
openai.api_type = 'azure'
openai.api_version = os.getenv('AZURE_OPENAI_API_VERSION')

# How many runs?
num_iterations = 10  # Number of times to send the prompt

def get_code_response(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-4-code-interpreter",  # Use the deployment name for the model
        messages=[
            {"role": "system", "content": "You are an AI programming assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def main():
    # Load the JSON file
    with open('tests.json', 'r') as file:
        data = json.load(file)

    for test in data['tests']:
        test_title = test['title']
        test_folder = os.path.join('output', test_title)
        os.makedirs(test_folder, exist_ok=True)

        prefix = test.get('prefix', '')

        for prompt in test['prompts']:
            prompt_folder = os.path.join(test_folder, prompt.replace(" ", "_"))
            os.makedirs(prompt_folder, exist_ok=True)

            unique_responses = set()

            for _ in range(num_iterations):
                full_prompt = f"{prefix} {prompt}".strip()
                response = get_code_response(full_prompt)
                if response not in unique_responses:
                    unique_responses.add(response)
                    filename = os.path.join(prompt_folder, f"{uuid.uuid4()}.txt")
                    with open(filename, 'w') as response_file:
                        response_file.write(response)
                time.sleep(1)  # To avoid hitting rate limits

if __name__ == "__main__":
    main()