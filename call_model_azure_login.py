"""
This script sends one prompt to a model deployed in Azure AI Foundry.
Authentication by Azure login. No API key needed.

Run:
    python call_model_azure_login.py
"""

import tomllib

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

# Load endpoint and deployment name from the config file
with open("azure_config.toml", "rb") as f:
    config = tomllib.load(f)["azure_openai"]

# Fetches (and refreshes) tokens from your `az login` session
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(base_url=config["endpoint"], api_key=token_provider)

response = client.chat.completions.create(
    model=config["deployment"],  # deployment name, not the model family
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "In one short paragraph, how can the Azure AI Foundry help research at Northwestern University?"},
    ],
)

print(response.choices[0].message.content)
