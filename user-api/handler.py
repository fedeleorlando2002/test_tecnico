import json
import boto3
from botocore.exceptions import ClientError

# Inizializzazione della risorsa DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = 'user-api-dev'  # Assicurati che corrisponda al nome della tua tabella
table = dynamodb.Table(table_name)

def createUser(event, context):
    # Caricamento dei dati dal corpo della richiesta
    data = json.loads(event['body'])

    # Controllo dei campi obbligatori
    if 'id' not in data or 'name' not in data or 'email' not in data:
        return {
            "statusCode": 400,  # Codice di stato HTTP per richiesta non valida
            "body": json.dumps({"messagio": "Campi obbligatori mancanti"})  # Messaggio di errore
        }

    # Controllo se l'ID esiste già
    try:
        response = table.get_item(Key={'id': data['id']})
        if 'Item' in response:
            return {
                "statusCode": 400,  # Codice di stato HTTP per richiesta non valida
                "body": json.dumps({"messagio": "Utente con questo id esiste già"})  # Messaggio di errore
            }
    except ClientError as e:
        return {
            "statusCode": 500,  # Codice di stato HTTP per errore interno del server
            "body": json.dumps({"message": str(e)})  # Messaggio di errore
        }

    # Creazione dell'elemento da inserire nella tabella
    item = {
        'id': data['id'],
        'name': data['name'],
        'email': data['email']
    }

    try:
        # Inserimento dell'elemento nella tabella DynamoDB
        table.put_item(Item=item)
        return {
            "statusCode": 201,  # Codice di stato HTTP per creazione riuscita
            "body": json.dumps(item)  # Restituzione dell'elemento inserito
        }
    except ClientError as e:
        # Gestione degli errori di AWS DynamoDB
        return {
            "statusCode": 500,  # Codice di stato HTTP per errore interno del server
            "body": json.dumps({"message": str(e)})  # Messaggio di errore
        }

def getUserById(event, context):
    # Recupero dell'ID dell'utente dai parametri del percorso
    user_id = event['pathParameters']['id']

    try:
        # Ottenimento dell'elemento dalla tabella DynamoDB
        response = table.get_item(Key={'id': user_id})
        if 'Item' in response:
            return {
                "statusCode": 200,  # Codice di stato HTTP per richiesta riuscita
                "body": json.dumps(response['Item'])  # Restituzione dell'elemento trovato
            }
        else:
            return {
                "statusCode": 404,  # Codice di stato HTTP per elemento non trovato
                "body": json.dumps({"messagio": "Utente non trovato"})  # Messaggio di errore
            }
    except ClientError as e:
        # Gestione degli errori di AWS DynamoDB
        return {
            "statusCode": 500,  # Codice di stato HTTP per errore interno del server
            "body": json.dumps({"message": str(e)})  # Messaggio di errore
        }
