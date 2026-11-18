# Workshop - LLMs on Azure

Repository for LLMs on Azure workshop

## Setup

The scripts require **Python 3.11 or newer** (they use the built-in `tomllib` module).

You will need to install `azure-identity`, and `openai`. You can use your favorite package manager or follow the steps below. I'll assume you have python and pip installed.

### STEP 1

On your terminal, go to this project's directory, and type:

```bash
python -m venv .venv
```
(on Mac you may need to type `python3` instead if `python` doesn't work).

This will create a virtual environment.

### STEP 2
Activate the environment:

```bash
# On Mac
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat
```

### STEP 3
Install the necessary packages.

```bash
pip install azure-identity openai
```

### STEP 4

Authenticate to Azure.

To authenticate to Azure from your computer, you will first need the azure cli tool. You can follow [Microsoft's Azure cli installation instructions](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest). Once installation is successful, follow the steps [in the Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) to authenticate using `az login`, which will redirect you to login using the browser.

(Note: If you're running this from quest, where no browser is available, choose the option:
`az login --use-device-code`).

You can also use the API key instead of authenticating, but we recommend the method above.

### STEP 5
Run the script:

```bash
python call_model_azure_login.py
```

## Note on user permissions

Your account also needs the appropriate permissions in order to call Foundry models. The specific permission depends on the authentication method (Azure CLI login as above, or through API keys), and the resource type. Look into Azure documentation for specifics.

Common roles include **Foundry User** and **Cognitive Services User** on the Foundry resource. The management roles **Owner** or **Contributor** alone are not enough to call the model with your Azure CLI authentication. If your role lacks the appropriate permissions, you're likely to encounter a 401/403 error.

