import azure.functions as func
import json
import os
from azure.cosmos import CosmosClient

COSMOS_DB_URL = os.getenv("COSMOS_DB_URL")
COSMOS_DB_KEY = os.getenv("COSMOS_DB_KEY")
DATABASE_NAME = "MovieCatalog"
CONTAINER_NAME = "Movies"

client = CosmosClient(COSMOS_DB_URL, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        movies = list(container.read_all_items())
        return func.HttpResponse(json.dumps(movies), mimetype="application/json", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
