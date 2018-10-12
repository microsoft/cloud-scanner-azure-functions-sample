# Cloud Resource Scanner - Azure Function App

This is an example Azure Function App that demonstrates the use of the [cloud-scanner]() library and its providers. [cloud-scanner]() is a Python package that pulls cloud resources from different providers (Azure, AWS, GCP) and puts the metadata into data stores.

## Running Locally
1. Clone necessary repos (this one included) to same directory
   - [cloud-scanner-functions]()
   - [cloud-scanner]()
   - [cloud-scanner-generic]()
   - [cloud-scanner-azure]()
2. Create Python 3.6 virtualenv `env` with all dependencies installed
    ```
    python3.6 -m virtualenv env
    source env/bin/activate
    (env) pip install -r requirements.txt
    ```
   If running on Windows CMD Prompt/Powershell:
   ```
   python3.6 -m virtualenv env
   .env\Scripts\activate
   (env) pip install -r requirements.txt
   ```
3. Create an [Azure Service Principal](docs/md/service-principal.md)
4. Create `.env` file in root directory and populate with appropriate data:
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
5. Create `local.settings.json` file in root directory and populate:
   ```json
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "<azure-storage-connection-string",
            "FUNCTIONS_WORKER_RUNTIME": "python"
        }
    }
   ```
6. Generate cloud config file
   ```bash
   (env) generate-config -p <cloud-provider1,cloud-provider2> -t <resource-type1,resource-type2>
   ```
   Example: Generate config to pull all Azure resources
   ```bash
   (env) generate-config -p azure -t "*"
   ```
7. Install [Azure Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
8. Register binding types
   ```bash
   (env) func extensions install
   ```
9.  [Deploy](docs/md/deployment.md) necessary resources
10. Run Azure Functions locally
    ```bash
    (env) func host start
    ```

## Publish Function App to Azure

