Param( 
   [string]$prefix = $(Read-Host "Provide company/group prefix"),
   [string]$location = $(Read-Host "Provide location abbr"),
   [string]$environment = $(Read-Host "Provider environment DEV|TEST|PROD"),
   [string]$applicationName = $(Read-Host "Provider name for app")
 )

$resourceGroupName = $prefix + '-' + $location + '-' + $environment + '-' + $applicationName
az group create -l westus -n $resourceGroupName

az group deployment create --resource-group $resourceGroupName --name cloud-scanner --template-file deploy.azure.json  --parameters parameters.json