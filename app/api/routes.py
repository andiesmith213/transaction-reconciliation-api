'''
Contains FastAPI routes that will call the service layer to process the transaction.
First rev of this file will have one route that reconciles the entire transaction.
Future revisions will have separate routes for different functionalities.
'''

from fastapi                            import APIRouter, HTTPException
from app.models.schemas                 import PendingTransaction
from app.services.reconcile_transaction import reconcile_tx
from app.services.process_transaction   import add_tx, get_tx_list, delete_pending_tx
from app.services.report_transaction    import get_issue_log

router = APIRouter()

#Endpoint to handle adding a new transaction
@router.put("/add/{source}")
def add(tx: PendingTransaction, source: str):
    if source not in ["processed", "internal"]:                  
        raise HTTPException(status_code=404, detail="Unknown transaction source. No transaction to add.")
    return add_tx(tx, source)

#Endpoint to handle returning pending list
@router.get("/get_pending_list/{source}")
def get_list(source: str):
    if source not in ["processed", "internal", "all"]:
        raise HTTPException(status_code=404, detail="Unknown transaction source. No list to return.")
    return get_tx_list(source)

#Endpoint to handle reconciling (matching + validating) the transaction
@router.post("/reconcile/{tx_id}")
def reconcile(tx_id: int, time_tolerance: float = 10, amount_tolerance: float = 0.5):      #Default of 10 minute tolerance between timestamps
    return reconcile_tx(tx_id, time_tolerance, amount_tolerance)

#Endpoint to allow for retrieving issue log
@router.get("/log/issues/{tx_id}")
def issue_log(tx_id: int):
    return get_issue_log(tx_id)

#Endpoint to allow for deleting a pending transaction
@router.delete("/delete/{source}/{tx_id}")
def delete_pending(source: str, tx_id: int):
    if source not in ["processed", "internal", "all"]:
        raise HTTPException(status_code=404, detail="Unknown transaction source.")
    return delete_pending_tx(tx_id, source)