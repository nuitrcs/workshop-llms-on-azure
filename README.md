# Workshop - LLMs on Azure

Repository for LLMs on Azure workshop

## Authenticating to Azure

To authenticate to Azure from your computer, follow the steps [in the Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest).

This will prompt you to login using the browser. If you're running this from quest, where no browser is available, choose the option:
```bash
az login --use-device-code
```

## Needed libraries

You will need to install `azure-identity`, and `openai` with your favorite package manager.