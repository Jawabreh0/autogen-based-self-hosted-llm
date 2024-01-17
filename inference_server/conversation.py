import requests

# Set the URL of your LLM server's inference endpoint
server_url = "http://localhost:8000/api/v1/chat/completions"

# Get the user's prompt input
user_prompt = input("Enter your prompt: ")

# Define the message with the user's input prompt
message = {
    "role": "user",
    "content": user_prompt
}

# Create the request payload
request_payload = {
    "messages": [message],
    "model": "/home/jawabreh/Desktop/CyprusCodes/CyprusCodes_LLM/mistral-7b-openorca.Q5_K_M.gguf"  
}

# Send a POST request to the server
response = requests.post(server_url, json=request_payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and display the generated response
    response_data = response.json()
    generated_response = response_data["choices"][0]["message"]["content"]
    print("Generated Response:")
    print(generated_response)
else:
    print("Error: Request to the server failed with status code:", response.status_code)
