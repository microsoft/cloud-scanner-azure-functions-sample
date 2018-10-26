# Cloud Scanner - Azure Functions Sample App

[![Build Status](https://travis-ci.com/Microsoft/cloud-scanner-azure-functions-sample.svg?branch=master)](https://travis-ci.com/Microsoft/cloud-scanner-azure-functions-sample)

This is an example Azure Function App that demonstrates the use of the [cloud-scanner](https://github.com/Microsoft/cloud-scanner) library and its providers. [cloud-scanner](https://github.com/Microsoft/cloud-scanner) is a Python package that pulls cloud resources from different providers (Azure, AWS, GCP) and puts the metadata into data stores.

**Note: This library is NOT affiliated with the Azure team at Microsoft and was developed by the Commercial Software Engineering team as a tool for the Open Source community to use and contribute to as they see fit. Use at your own risk!**

## Related Projects
The following are a list of related projects that are dependencies for the Azure Functions sample:

1. [`cloud-scanner`](https://github.com/Microsoft/cloud-scanner)
    
    Core library components for cloud-scanner project
2. [`cloud-scanner-azure`](https://github.com/Microsoft/cloud-scanner-azure)

    Azure components for cloud-scanner project. Includes Azure support for discovering Azure resources in addition to storage and workflow components for hosting on Azure
3. [`cloud-scanner-generic`](https://github.com/Microsoft/cloud-scanner-generic)

    Generic components for cloud-scanner project including MySql, ElasticSearch and more

## Running Locally
1. Create Python 3.6 virtualenv `env` with all dependencies installed
    ```
    python3.6 -m virtualenv env
    source env/bin/activate
    (env) pip install -r requirements.txt
    (env) pip install -r requirements-dev.txt
    ```
   If running on Windows CMD Prompt/Powershell:
   ```
   python3.6 -m virtualenv env
   .env\Scripts\activate
   (env) pip install -r requirements.txt
   (env) pip install -r requirements-dev.txt
   ```
2. Create an [Azure Service Principal](docs/md/service-principal.md)
3. Create `.env` file in root directory and populate with appropriate data:
    ```
    # Azure authentication
    AZURE_CLIENT_ID=<service-principal-app-id>
    AZURE_CLIENT_SECRET=<service-principal-secret>
    AZURE_STORAGE_ACCOUNT=<azure-storage-account-name>
    AZURE_STORAGE_KEY=<azure-storage-account-key
    AZURE_TENANT_ID=<service-principal-tenant-id>
    AzureWebJobsStorage=<azure-storage-connection-string>

    # Container & Queue Names
    CONFIG_CONTAINER=config-files
    PAYLOAD_QUEUE_NAME=resource-payloads
    TAG_UPDATES_QUEUE_NAME=resource-tag-updates
    TASK_QUEUE_NAME=resource-jobs

    # Resource types
    RESOURCE_STORAGE_TYPE=rest_storage_service
    STORAGE_CONTAINER_TYPE=azure_storage
    QUEUE_TYPE=azure_storage_queue

    # Needed for 'rest_storage_service' storage type
    REST_STORAGE_URL=<api-url-for-posting-resources>
    
    # App Insights (optional)
    APPINSIGHTS_APPID=<app-insights-app-id>
    APPINSIGHTS_INSTRUMENTATIONKEY=<app-insights-instrumentation-key>
    ```
4. Create `local.settings.json` file in root directory and populate:
   ```json
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "<azure-storage-connection-string",
            "FUNCTIONS_WORKER_RUNTIME": "python"
        }
    }
   ```
5. Generate cloud config file
   ```bash
   (env) generate-config -p <cloud-provider1,cloud-provider2> -t <resource-type1,resource-type2>
   ```
   Example: Generate config to pull all Azure resources
   ```bash
   (env) generate-config -p azure -t "*"
   ```
6. Install [Azure Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
7. Register binding types
   ```bash
   (env) func extensions install
   ```
8.  [Deploy](docs/md/deployment.md) necessary resources
9.  Run Azure Functions locally
    ```bash
    (env) func host start
    ```

## Publish Function App to Azure

#### Azure Resources

The Azure Functions Sample runs on a Linux consumption plan with python support.  The ARM template is complete and deploys the following resources:
- Functions App
- Linux Consumption App Service Plan
- Storage Account
- Application Insights

Automatically deploy using the `deployments/deploy.ps1` or the following Azure CLI commands.
```powershell
$resourceGroupName = <resource-group-name>
az group create -l westus -n $resourceGroupName

az group deployment create 
    --resource-group $resourceGroupName 
    --name cloud-scanner 
    --template-file deploy.azure.json 
    --parameters parameters.json 
    --parameters 
        prefix=$prefix 
        location_abbr=$locationAbbr 
        environment=$environment 
        application_name=$applicationName
```

#### Deploying Function App Code

This repo is set up to use Travis CI to deploy code from the `master` branch. In order for this to work properly, you will need to use the service principal created previously (or create a new one) and add the following environment variables to your Travis settings with the appropriate values: 

```
AZ_SP_ID=<service-principal-app-id>
AZ_SP_SECRET=<service-principal-secret>
AZ_TENANT_ID=<service-principal-tenant-id>
GITHUB_TOKEN=<github-token>
AZ_FUNCTIONS_APP_NAME=<name-of-functions-app>
```

To deploy from your machine, create and activate your virtual environment and run:

```bash
func azure functionapp publish <your-function-app-name> --build-native-deps --force
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
