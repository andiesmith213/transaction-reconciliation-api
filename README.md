# Overview
## Purpose
This is a server side app that can be used to reconcile differences in financial transactions between an internal system ledger and the actual processed transaction. Specifically, this app will compare differences in 
the timestamps and amounts against a user provided tolerance, and will return any discrepancies within the internal versus processed transactions. 

## System Diagram
<img width="1265" height="726" alt="image" src="https://github.com/user-attachments/assets/ca47069c-732a-444c-be7b-964fc3e7ee69" />

### Process service
<img width="1305" height="622" alt="image" src="https://github.com/user-attachments/assets/b1cb2aa3-51fe-4e2c-9091-6ad4619fab32" />

### Reconcile service 
<img width="1329" height="633" alt="image" src="https://github.com/user-attachments/assets/c3ea79a4-05cf-4750-a92e-55dfe8f94138" />

### Report service
<img width="952" height="369" alt="image" src="https://github.com/user-attachments/assets/b6d51d78-a385-4bc1-9b2a-793f78e8ecd1" />




## Available requests
> Add new pending transaction 

> Return list of all pending transactions

> Reconcile transaction based off ID

> Retrieve a log of issues based off ID

> Delete existing pending transaction

# Running the app
This app is designed to run from the root directory that contains the app and tests folder.
If you clone this project into a folder named something other than transaction_reconciliation_api, change where you see [transaction_reconciliation_api] with your project name.
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
From root directory:
> pytest --cov --cov-report=html
