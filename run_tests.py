import os
import requests  
import time
import json
import uuid
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_BASE = os.environ.get("AZURE_OPENAI_API_BASE")
DEPLOYMENT = os.environ.get("AZURE_OPENAI_API_MODEL")
API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION")
API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
ENDPOINT = API_BASE + "openai/deployments/" + DEPLOYMENT + "/chat/completions?api-version=" + API_VERSION

# headers
headers = {  
    "Content-Type": "application/json",  
    "api-key": API_KEY  
}  

# configuration
temperature = 0.95
top_p = 0.95
num_iterations = 10  # Number of times to send the prompt
sleep_time = 10  # Time to sleep between requests

instructions = [
  "You are an AI programming assistant.",
  "You return only code snippets with NO OTHER TEXT, code fences, etc.",
  "Assume your responses will be used in a code editor within an existing HTML document.",
  # "Your responses only include the amount of HTML required to properly and validly fulfill the request.",
  "You may include inline CSS or JavaScript, but only as much as absolutely necessary."
]

def get_code_response(prompt):
    print(f"Prompt: {prompt}")
    payload = {
      "messages": [
        {
          "role": "system",
          "content": [{
            "type": "text",
            "text": " ".join(instructions)
          }]
        },
        {
          "role": "user",
          "content": [{
            "type": "text",
            "text": prompt
          }]
        }
      ],
      "temperature": temperature,
      "top_p": top_p,
      "max_tokens": 800
    }  

    try:  
      response = requests.post(ENDPOINT, headers=headers, json=payload)  
      response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code  
    except requests.RequestException as e:  
      raise SystemExit(f"Failed to make the request. Error: {e}")  
  
    result = response.json()
    code = result['choices'][0]['message']['content']
    print(f"Response: {code}")
    return code

def main():
    # Load the JSON file
    with open('tests.json', 'r') as file:
        data = json.load(file)

    for test in data['tests']:
        test_title = test['title']
        test_folder = os.path.join('output', test_title)
        os.makedirs(test_folder, exist_ok=True)

        prefix = test.get('prefix', '')

        for prompt_index, prompt in enumerate(test['prompts'], start=1):
            prompt_folder = os.path.join(test_folder, str(prompt_index))
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
                time.sleep(sleep_time)  # To avoid hitting rate limits

if __name__ == "__main__":
    main()