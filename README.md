# Overview
This app will reconcile differences in transactions between the internal system ledger and actual processed transaction. Specifically, this app will compare differences in 
the timestamps and amounts against a user provided tolerance, and will return any discrepancies within the internal versus processed transactions. 

Currently available requests:
- Add new pending transaction 
- Return list of all pending transactions
- Reconcile transaction based off ID
- Match a pending and internal transaction based off provided ID
- Validate timestamp based off ID
- Validate amount based off ID
- Retrieve a log of issues based off ID
- Delete existing pending transaction

# Running the app
This app is designed to run from the root directory that contains the app and tests folder.
If you clone this project into a folder named something other than transaction_reconciliation_api, change commands that say [transaction_reconciliation_api] with your project name.
## Using Docker Container
Build docker image
> docker build -t [transaction_reconciliation_api] .

Run with docker
> docker run -p 8000:8000 [transaction_reconciliation_api]
## Manually
Install dependencies
> pip install -r requirements.txt

Run app from root
> uvicorn app.main:app

# Testing
from transaction_reconciliation_api:
> pytest --cov --cov-report=html
