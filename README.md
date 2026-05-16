# Overview
## Purpose
This is a server side app that can be used to reconcile differences in financial transactions between an internal system ledger and the actual processed transaction. Specifically, this app will compare differences in 
the timestamps and amounts against a user provided tolerance, and will return any discrepancies within the internal versus processed transactions. 

### Interacting with app
The transaction-reconciliation-api was built using the FastAPI web framework. To demo the behavior of available endpoints, use fastAPI's built-in docs page while running the app: 
> http://127.0.0.1:8000/docs

Additionally, videos demonstrating the app can be found throughout this README. 

## System Diagram
<img width="1265" height="726" alt="image" src="https://github.com/user-attachments/assets/ca47069c-732a-444c-be7b-964fc3e7ee69" />

### Process service
<img width="1305" height="622" alt="image" src="https://github.com/user-attachments/assets/b1cb2aa3-51fe-4e2c-9091-6ad4619fab32" />

https://github.com/user-attachments/assets/1ef9eff8-ff31-4c0a-94d5-63aaad3b3894

https://github.com/user-attachments/assets/168456c5-1ac8-44d0-923b-161d4731d94d

https://github.com/user-attachments/assets/82a498a7-50be-4022-9ec9-4f3ad805dba9


### Reconcile service 
<img width="1329" height="633" alt="image" src="https://github.com/user-attachments/assets/c3ea79a4-05cf-4750-a92e-55dfe8f94138" />

### Report service
<img width="927" height="373" alt="image" src="https://github.com/user-attachments/assets/10317607-076d-43b9-ba7b-d5d8ee7fb139" />

## Available requests
- Add new pending transaction 
- Return pending transactions based off ID or source
- Delete existing pending transaction
- Reconcile transaction based off ID
- Retrieve a log of issues found during reconciling based off ID

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

## Coverage
<a href="[URL](https://github.com/andiesmith213/transaction-reconciliation-api/blob/master/reports/coverage/index.html)">Coverage Report</a>
