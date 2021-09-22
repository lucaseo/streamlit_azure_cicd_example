


## 1. Install Azure Cli and login


```bash
# mac ver
brew install azure-cli
az login
```


## 2. Build and push to ACR

```bash
az acr build --registry {REGISTRY_NAME} --image {IMAGE_NAME} ./
```


## 3. Create Web App

- Azure: App Services
- Publish : Docker Container
- Operaing System: Linux
- Sku and size: Basic B1
- Option: Single Container
- Image Source: Azure Container Registry
