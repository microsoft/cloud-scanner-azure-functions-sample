az login --service-principal --username "$APP_ID" --password "$AZ_SP_SECRET" --tenant "$AZ_TENANT_ID"
az account get-access-token --query "accessToken"
func azure functionapp publish $AZ_FUNCTIONS_APP_NAME --build-native-deps --force
