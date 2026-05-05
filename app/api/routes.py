'''
Contains FastAPI routes that will call the service layer to process the transaction.
First rev of this file will have one route that reconciles the entire transaction.
Future revisions will have separate routes for different functionalities.
'''

from fastapi                            import APIRouter, HTTPException
from models.schemas                     import PendingTransaction
from services.reconcile_transaction     import reconcile_tx
from services.process_transaction       import add_tx, get_tx

router = APIRouter()

#Endpoint to handle adding a new transaction
@router.put("/add/{source}")
def add(tx: PendingTransaction, source: str):
    src = source.lower()                                    #.lower() to avoid mismatches due to case sensitivity
    if src not in ["processed", "internal"]:                  
        raise HTTPException(status_code=404, detail="Unknown transaction source. No transaction to add.")
    return add_tx(tx, src)

#Endpoint to handle returning pending list
@router.get("/get_list/{source}")
def get_list(source: str):
    src = source.lower()                                    #.lower() to avoid mismatches due to case sensitivity
    if src not in ["processed", "internal", "all"]:
        raise HTTPException(status_code=404, detail="Unknown transaction source. No list to return.")
    return get_tx(src)

#Endpoint to handle reconciling the transaction
@router.post("/reconcile/{tx_id}")
def reconcile(tx_id: int):
    return reconcile_tx(tx_id)

#TODO: add issues and matches endpoints once reconciliation portion is done
#TODO: is there a way to add in a check that occurs before the app is shut down?
    #If so, add check of pending transaction indexes to confirm no transactions were missed