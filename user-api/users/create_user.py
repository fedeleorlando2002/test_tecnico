import json
import boto3
import uuid
from botocore.exceptions import ClientError

# Inizializzazione della risorsa DynamoDB
dynamodb = boto3.resource('dynamodb')
# Nome della tabella DynamoDB deve corrispondere a quello definito in serverless.yml
table = dynamodb.Table('user-api-dev')

def create_user(event):
    # Caricamento del corpo della richiesta JSON
    body = json.loads(event['body'])
    # Generazione di un nuovo UUID per l'utente
    user_id = str(uuid.uuid4())
    # Creazione dell'oggetto utente
    user = {
        'id': user_id,
        'name': body['name'],
        'email': body['email']
    }
    
    try:
        # Inserimento dell'oggetto utente nella tabella DynamoDB
        table.put_item(Item=user)
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 201,  # Codice di stato HTTP per risorsa creata
        'body': json.dumps(user)  # Restituzione dell'utente creato come JSON
    }