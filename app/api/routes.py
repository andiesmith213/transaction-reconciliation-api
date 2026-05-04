'''
Contains FastAPI routes that will call the service layer to process the transaction.
First rev of this file will have one route that reconciles the entire transaction.
Future revisions will have separate routes for different functionalities.
'''

from fastapi                            import APIRouter
from models.schemas                     import PendingTransaction
from services.reconcile_transaction     import reconcile_tx
from services.add_transaction           import add_tx

router = APIRouter()

# #Endpoint to handle reconciling the transaction
# @router.post("/ingest")
# def ingest(tx: PendingTransaction):
#     result = reconcile_tx(tx)
#     return result

#Endpoint to handle adding a new transaction
@router.put("/add")
def add(tx: PendingTransaction):
    add_tx(tx)