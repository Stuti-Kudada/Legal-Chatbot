import requests
import os
from dotenv import load_dotenv

# Load environment variables (for API key security)
load_dotenv()

# Retrieve the Vultr API key from the environment
VULTR_API_KEY = os.getenv("VULTR_API_KEY2")

headers = {
    "Authorization": f"Bearer {VULTR_API_KEY}",
    "Content-Type": "application/json"
}

# Function to retrieve details for a specific model
def get_model_details(model_id):
    url = f"https://api.vultrinference.com/v1/models/{model_id}"
    response = requests.get(url, headers=headers)
    
    # Print response to view model details
    print("Model details:", response.json())
    return response.json()

# Function to perform inference using the model
def run_inference(model_id, prompt):
    url = f"https://api.vultrinference.com/v1/chat/completions/RAG"
    payload = {
        "model": model_id,
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Print response to view inference result
    print("Inference result:", response.json())
    return response.json()

# Example usage
if __name__ == "__main__":
    # Define the model ID and prompt for testing
    model_id = "zephyr-7b-beta-f16"
    prompt = "Explain the importance of data privacy in legal documents."

    # Retrieve model details
    model_details = get_model_details(model_id)
    
    # Run inference with the specified prompt
    inference_result = run_inference(model_id, prompt)