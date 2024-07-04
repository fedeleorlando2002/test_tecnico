import json
import boto3

# Inizializzazione della risorsa DynamoDB
dynamodb = boto3.resource('dynamodb')
# Nome della tabella DynamoDB deve corrispondere a quello definito in serverless.yml
table = dynamodb.Table('user-api-dev')

def get_user(event):
    # Recupero dell'ID dell'utente dai parametri del percorso
    user_id = event['pathParameters']['id']
    
    # Ottenimento dell'elemento dalla tabella DynamoDB
    response = table.get_item(
        Key={
            'id': user_id
        }
    )
    
    if 'Item' in response:
        return {
            'statusCode': 200,  # Codice di stato HTTP per richiesta riuscita
            'body': json.dumps(response['Item'])  # Restituzione dell'utente trovato come JSON
        }
    else:
        return {
            'statusCode': 404,  # Codice di stato HTTP per risorsa non trovata
            'body': json.dumps({'errore': 'Utente non trovato'})  # Messaggio di errore
        }
