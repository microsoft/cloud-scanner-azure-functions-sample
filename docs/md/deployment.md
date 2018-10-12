# Azure Deployment

Using the Azure CLI, either from inside the Azure Portal using Cloud Shell in Powershell Mode, or [locally](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

1. Populate [ARM template](Deployment/deploy.azure.json) with necessary info from `.env`
2. Deploy ARM template
3. Verify resources and settings in Azure portal

Currently, timer trigger functions (`RunRules` and `TaskScheduler`) are set to run every 5 minutes. That is set in the `function.json` files.

[![Visualize](http://armviz.io/visualizebutton.png)]()
[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)]()
