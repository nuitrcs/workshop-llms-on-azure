"""
This script sends one prompt to a model deployed in Azure AI Foundry,
authenticating with an API key.

Put your key in an environment variable (never in this file or the toml):
    export AZURE_OPENAI_API_KEY="..."

Or save it in a .env file (making sure you add it to .gitignore),
and modify the script to load the key from there.

Run:
    python call_model_api_key.py

NOTE: this file is for exposition purposes and was not tested.
"""

import os
import tomllib

from openai import OpenAI

# Load endpoint and deployment name from the config file
with open("azure_config.toml", "rb") as f:
    config = tomllib.load(f)["azure_openai"]

client = OpenAI(
    base_url=config["endpoint"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    model=config["deployment"],  # deployment name, not the model family
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "In one sentence, what is Azure AI Foundry?"},
    ],
)

print(response.choices[0].message.content)
