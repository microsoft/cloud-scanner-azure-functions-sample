Param(
   [string]$prefix = $(Read-Host("Company/Group prefix for resource naming")),
   [string]$locationAbbr = $(Read-Host("Location abbreviation for resource naming")),
   [string]$environment = $(Read-Host("Environment DEV|TEST|PROD")),
   [string]$applicationName = $(Read-Host("Application Name"))
)

$resourceGroupName = $prefix + '-' + $locationAbbr + '-' + $environment + '-' + $applicationName
az group create -l westus -n $resourceGroupName
az group deployment create --resource-group $resourceGroupName --name cloud-scanner --template-file deploy.azure.json --parameters parameters.json --parameters prefix=$prefix location_abbr=$locationAbbr environment=$environment application_name=$applicationName