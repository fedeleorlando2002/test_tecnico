1. Configurazione dell'Ambiente di Sviluppo
-AWS Account: Registrazione e configurazione di un account AWS.
-AWS CLI: Installazione e configurazione dell'AWS CLI con aws configure.
-Serverless Framework: Installazione del Serverless Framework globalmente con npm install -g serverless.

2. Creazione del Progetto con Serverless Framework
-Creazione del Progetto: Utilizzo del comando serverless create --template aws-python3 --path user-api per creare un nuovo progetto Serverless.

3. Configurazione del File serverless.yml
-Definizione del Servizio: Configurazione del nome del servizio, provider, runtime, regione e variabili d'ambiente.
-Funzioni Lambda: Definizione delle funzioni createUser e getUserById con i rispettivi handler e eventi HTTP (POST e GET).
-Risorse AWS: Configurazione delle risorse DynamoDB per creare una tabella user-api-dev.

4. Implementazione dei Gestori delle Funzioni Lambda (handler.py)
-createUser: Funzione per creare un nuovo utente e inserirlo nella tabella DynamoDB.
-getUserById: Funzione per recuperare un utente dalla tabella DynamoDB tramite il suo ID.

5. Deploy delle Risorse su AWS
-Deploy: Utilizzo del comando serverless deploy per creare le risorse AWS e caricare le funzioni Lambda.

6. Verifica del Deploy su AWS
-Console AWS: Verifica della creazione delle funzioni Lambda, della tabella DynamoDB e della configurazione degli endpoint API Gateway.
-Controllo dei Permessi: Assicurazione che le politiche IAM permettano alle funzioni Lambda di interagire con DynamoDB.

7. Test delle API con Postman
-Endpoint POST: Test dell'endpoint POST /users per creare un nuovo utente.
-Endpoint GET: Test dell'endpoint GET /users/{id} per recuperare un utente tramite ID.

8. Risoluzione dei Problemi
-Log e Debug: Utilizzo di CloudFormation e CloudWatch per monitorare e risolvere eventuali problemi durante il deploy e l'esecuzione delle funzioni Lambda.
-Permessi IAM: Aggiunta di politiche IAM per garantire che le funzioni Lambda abbiano i permessi necessari per accedere a DynamoDB.


Conclusioni
Abbiamo configurato e deployato con successo un set di REST API utilizzando AWS Lambda, DynamoDB e API Gateway, gestiti tramite Serverless Framework e scritti in Python. Abbiamo anche verificato il funzionamento delle API con Postman e risolto eventuali problemi relativi ai permessi IAM.
