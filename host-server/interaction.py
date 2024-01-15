import requests

# Define the server URL
server_url = "http://localhost:8000"  # Replace with your server's URL

# Example 1: Send a GET request to the root URL
response = requests.get(f"{server_url}/")
print(response.text)

# Example 2: Send a POST request to an endpoint
payload = {
    "messages": [
        {"role": "user", "content": "Hello, LLM!"},
        {"role": "assistant", "content": ""},
    ],
    "model": "/home/jawabreh/Desktop/CyprusCodes/CyprusCodes_LLM/mistral-7b-openorca.Q5_K_M.gguf",
}
response = requests.post(f"{server_url}/api/v1/chat/completions", json=payload)
print(response.json())
