'''
Contains FastAPI routes that will call the service layer to process the transaction.
First rev of this file will have one route that reconciles the entire transaction.
Future revisions will have separate routes for different functionalities.
'''

from fastapi                            import APIRouter
from models.schemas                     import PendingTransaction, TransactionID
from services.reconcile_transaction     import reconcile_tx
from services.handle_transaction        import add_tx, get_tx

router = APIRouter()

#Endpoint to handle adding a new transaction
@router.put("/add")
def add(tx: PendingTransaction):
    add_tx(tx)

#Endpoint to handle returning pending list
@router.get("/get_list/{source}")
def get_list(source: str):
    return get_tx(source)

# #Endpoint to handle reconciling the transaction
# @router.post("/reconcile")
# def reconcile(tx_id: TransactionID):
#     result = reconcile_tx(tx_id.tx_id)
#     return result