import os 
from dotenv import load_dotenv

# 加載 .env 文件
load_dotenv()


# required
subscription_id = os.environ['SUBSCRIPTION_ID']
tenant_id = os.environ['TENANT_ID']
service_principal_id = os.environ['AZURE_SERVICE_PRINCIPAL_APPID']
service_principal_password = os.environ['AZURE_SERVICE_PRINCIPAL_PASSWORD']

# optional
resource_group = os.environ('RESOURCE_GROUP', default='demo-try-azureml')
workspace_name = os.environ('WORKSPACE_NAME', default='demo-try-azureml')
workspace_region = os.environ('WORKSPACE_REGION', default='eastus2')


