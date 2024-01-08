import requests
import json
import os

# Replace with your OpenAI API key
OPENAI_API_KEY = ""

# Define the API endpoint and request payload
api_url = 'https://api.openai.com/v1/images/generations'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}
data = {
    "model": "dall-e-3",
    "prompt": "", 
    "n": 1,
    "size": "1024x1024"
}

# Start an infinite loop
while True:
    # Get the text description of the image from the user
    text = input("Enter the text description of the image (type 'exit' or 'quit' to stop): ")

    # Check if the user wants to exit
    if text.lower() in ['exit', 'quit']:
        break

    # Assign the text description to the data['prompt'] key
    data['prompt'] = text

    # Make the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        print("Generated image URL:", result['data'][0]['url'])
    else:
        print("Error:", response.status_code, response.text)
