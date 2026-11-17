# Workshop - LLMs on Azure

Repository for LLMs on Azure workshop

## Authenticating to Azure

To authenticate to Azure from your computer, follow the steps [in the Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest).

This will prompt you to login using the browser. If you're running this from quest, where no browser is available, choose the option:
```bash
az login --use-device-code
```

Your account also needs the **Cognitive Services OpenAI User** role (or **Azure AI User**) on the Foundry resource. Owner or Contributor alone is not enough to call the model with your Azure login. Without it, you'll get a 401/403 error. Roles are assigned in the Azure portal under the resource's **Access control (IAM)**.

## Needed libraries

The scripts require **Python 3.11 or newer** (they use the built-in `tomllib` module).

You will need to install `azure-identity`, and `openai` with your favorite package manager.