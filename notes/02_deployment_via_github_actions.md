# Azure App CI/CD with Github Actions


## 1. Connect to Github

1. App Service
2. Deployment Center 
   - Source - Github Actions 
   - Authenticate Github and select repository
   - [Reference](https://docs.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel#use-the-deployment-center)
3. Gen Deployment Credentials
   - App Service - Settings - Configuration
     - ADD
       - `WEBSITE_WEBDEPLOY_USE_SCM` = true 
   - App Service - Overview - Get Publish Profile
   - [Reference](https://docs.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel#generate-deployment-credentials)
4. Github - Settings - Secrets - New Repository Secrets
   - [Reference](https://docs.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel#configure-the-github-secret)
5. 