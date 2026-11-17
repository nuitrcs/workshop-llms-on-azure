# Workshop - LLMs on Azure

Repository for LLMs on Azure workshop

## Authenticating to Azure

To authenticate to Azure from your computer, follow the steps [in the Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest).

This will prompt you to login using the browser. If you're running this from quest, where no browser is available, choose the option:
```bash
az login --use-device-code
```

You can also use the API key instead of authenticating, but we recommend the method above.

## Note on user permissions

Your account also needs the appropriate permissions in order to call Foundry models. The specific permission depends on the authentication method (Azure CLI login as above, or through API keys), and the resource type. Look into Azure documentation for specifics.

Common roles include **Foundry User** and **Cognitive Services User** on the Foundry resource. The management roles **Owner** or **Contributor** alone are not enough to call the model with your Azure CLI authentication. If your role lacks the appropriate permissions, you're likely to encounter a 401/403 error.

## Needed libraries

The scripts require **Python 3.11 or newer** (they use the built-in `tomllib` module).

You will need to install `azure-identity`, and `openai` with your favorite package manager.