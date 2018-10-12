#### Creating an Azure Service principal

We use a service principal name (SPN) to perform Azure calls inside of the Azure Function. SPN's have no 
privileges by default and must be granted them for each subscription, resource group, or resource you 
wish for them to have access to.

1. Log in and set active subscription
   ```
   az login
   az account set --subscription <subscription-id>
   ```
2. Create service principal
   ```
    az ad sp create-for-rbac --name <spn-name> --password <spn-password>
    ```   
    This should return something like this:
    ```
    {
        "appId": <app-id>,
        "displayName": <spn-name>,
        "name": "http://<spn-name>",
        "password": <spn-password>,
        "tenant": <spn-tenant>
    }
    ```

If you would like the Service Principal to have access to multiple subscriptions, perform the following commands with each subscription ID:

```bash
az account set --subscription <subscription-id>
az role assignment create --assignee <app-id> --role Contributor
```

Roles can also be added/removed from inside the Azure Portal from the `Access Control (IAM)`
menu on any subscription, resource group, or resource.