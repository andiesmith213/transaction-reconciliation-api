'''
add_transaction.py handles adding pending transactions to the proper 
list within the pending queue.
'''
from fastapi import HTTPException
from storage.storage import pending

def add_tx(transaction):
    #Determine source of transaction and add to appropriate pending list
    if transaction.source.lower() == "internal":        #.lower() to avoid mismatches due to case sensitivity
        pending.set_internal_transaction(transaction)
        raise HTTPException(status_code=200, detail="Transaction {} logged as internal pending transaction".format(str(transaction.tx_id)))
    elif transaction.source.lower() == "processed":        #.lower() to avoid mismatches due to case sensitivity
        pending.set_processed_transaction(transaction)
        raise HTTPException(status_code=200, detail="Transaction {} logged as processed pending transaction".format(str(transaction.tx_id)))
    else:
        raise HTTPException(status_code=404, detail="Source of transaction could not be determined. Transaction not logged.")