'''
Contains FastAPI routes that will call the service layer to process the transaction.
First rev of this file will have one route that reconciles the entire transaction.
Future revisions will have separate routes for different functionalities.
'''

from fastapi                            import APIRouter, HTTPException
from app.models.schemas                 import PendingTransaction
from app.services.reconcile_transaction import reconcile_tx
from app.core.match_transaction         import match_events
from app.core.validate_transaction      import validate_timestamp
from app.services.process_transaction   import add_tx, get_tx_list

router = APIRouter()

#Endpoint to handle adding a new transaction
@router.put("/add/{source}")
def add(tx: PendingTransaction, source: str):
    if source not in ["processed", "internal"]:                  
        raise HTTPException(status_code=404, detail="Unknown transaction source. No transaction to add.")
    return add_tx(tx, source)

#Endpoint to handle returning pending list
@router.get("/get_list/{source}")
def get_list(source: str):
    if source not in ["processed", "internal", "all"]:
        raise HTTPException(status_code=404, detail="Unknown transaction source. No list to return.")
    return get_tx_list(source)

#Endpoint to handle reconciling (matching + validating) the transaction
@router.post("/reconcile/{tx_id}")
def reconcile(tx_id: int, time_tolerance: int = 10):      #Default of 10 minute tolerance between timestamps
    return reconcile_tx(tx_id, time_tolerance)

#Endpoint to allow for matching events
@router.post("/match/{tx_id}")
def match(tx_id: int):
    return match_events(tx_id)

#Endpoint to allow for validating timestamps
@router.get("/validate/time/{tx_id}")
def time(tx_id: int, tolerance: int = 10):      #Default of 10 minute tolerance between timestamps
    return validate_timestamp(tx_id, tolerance)

#TODO: add issues and matches endpoints once reconciliation portion is done
#TODO: add delete endpoint to delete a pending transaction
#TODO: is there a way to add in a check that occurs before the app is shut down?
    #If so, add check of pending transaction indexes to confirm no transactions were missed