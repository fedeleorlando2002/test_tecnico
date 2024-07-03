# User API

## Descrizione

Questo progetto implementa delle API REST per la creazione e visualizzazione di un modello utente. Utilizza AWS Lambda per l'elaborazione delle richieste, DynamoDB per la memorizzazione dei dati utente e API Gateway per l'esposizione delle API. Il progetto è sviluppato in Python e utilizza il framework Serverless per la gestione delle risorse AWS.

## Prerequisiti

- Account AWS
- Node.js e npm
- Serverless Framework
- Python 3.8+
- pip (Python package installer)

## Setup del Progetto

1. **Clona il repository:**

    ```sh
    https://github.com/fedeleorlando2002/test_tecnico.git
    cd user-api
    ```

2. **Crea un ambiente virtuale:**

    ```sh
    python -m venv .venv       # Su Windows: py -3 -m venv .venv
    source .venv/bin/activate  # Su Windows: .venv\Scripts\activate
    ```

3. **Installa le dipendenze:**

    ```sh
    pip install -r requirements.txt
    npm install -g serverless
    ```

4. **Configura le credenziali AWS:**

    Esegui il comando seguente e inserisci le tue credenziali AWS:

    ```sh
    aws configure
    ```

## Deploy del Progetto

1. **Configura Serverless Framework:**

    ```sh
    serverless config credentials --provider aws --key YOUR_ACCESS_KEY_ID --secret YOUR_SECRET_ACCESS_KEY
    ```

     Controllare YOUR_ACCESS_KEY_ID e YOUR_SECRET_ACCESS_KEY siano gli stessi credenziali su AWS.

2. **Deploy dell'applicazione:**

    ```sh
    serverless deploy
    ```

    Dopo il deploy, dovresti vedere gli endpoint API e le funzioni Lambda distribuite su AWS.

## Utilizzo delle API

### Create User

- **Metodo**: POST
- **URL**: `https://n4arthfeb1.execute-api.us-east-1.amazonaws.com/dev/users`
- **Corpo della richiesta** (JSON):

    ```json
    {
      "id": "1",
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Risposta** (201 - Created):

    ```json
    {
      "id": "1",
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

### Get User by ID

- **Metodo**: GET
- **URL**: `https://n4arthfeb1.execute-api.us-east-1.amazonaws.com/dev/users/{id}`

- **Risposta** (200 - OK):

    ```json
    {
      "id": "generated-uuid",
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Risposta** (404 - Not Found):

    ```json
    {
      "error": "User not found"
    }
    ```

## Struttura del Progetto

- `create_user.py`: Funzione Lambda per creare un nuovo utente.
- `get_user.py`: Funzione Lambda per ottenere un utente per ID.
- `serverless.yml`: Configurazione Serverless Framework per definire le risorse e le funzioni AWS.
