import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    endpoint = "https://azurecloud-resume.documents.azure.com:443"
    key = "AccountEndpoint=https://azurecloud-resume.documents.azure.com:443/;AccountKey=XSOKRpbBGB1iduf8WeY0YLtHgX6lPtfa8uTckDhK6KmkcopG2zFKgut24djVOJjR6DstyDdweNkUACDbyqfGhw==;"
    database_id = "AzureResume"
    container_id = "WebsiteCounter"
    partition_id = "1"

    client = CosmosClient(endpoint, key)
    container = client.get_database_client(database_id).get_container_client(container_id)

    if req.method == 'GET':
        try:
            item = container.read_item(partition_key=partition_id, item="count")
            count = item.get("count", 0)
            return func.HttpResponse(str(count))
        except Exception as e:
            logging.error(e)
            return func.HttpResponse("Count not found", status_code=404)

    elif req.method == 'POST':
        try:
            item = container.read_item(partition_key=partition_id, item="count")
            count = item.get("count", 0)
            count += 1
            item["count"] = count
            container.upsert_item(item)
            return func.HttpResponse(str(count))
        except Exception as e:
            logging.error(e)
            return func.HttpResponse("Error updating count", status_code=500)

    else:
        return func.HttpResponse("Invalid request", status_code=400)
