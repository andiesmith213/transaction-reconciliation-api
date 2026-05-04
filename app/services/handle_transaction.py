'''
handle_transaction.py performs the following: 
- adding pending transactions to the proper list
- returning list of pending transactions
'''
from fastapi import HTTPException
from storage.storage import pending

def add_tx(transaction):
    #Determine source of transaction and add to appropriate pending list
    if transaction.source.lower() == "internal":            #.lower() to avoid mismatches due to case sensitivity
        pending.set_internal_transaction(transaction)
        raise HTTPException(status_code=200, detail="Transaction {} logged as internal pending transaction".format(str(transaction.tx_id)))
    elif transaction.source.lower() == "processed":         #.lower() to avoid mismatches due to case sensitivity
        pending.set_processed_transaction(transaction)
        raise HTTPException(status_code=200, detail="Transaction {} logged as processed pending transaction".format(str(transaction.tx_id)))
    else:
        raise HTTPException(status_code=404, detail="Source of transaction could not be determined. Transaction not logged.")
    
def get_tx(source):
    #Return appropriate list based off source
    if source.lower() == "internal":            #.lower() to avoid mismatches due to case sensitivity
        return pending.get_internal_list()
    elif source.lower() == "processed":         #.lower() to avoid mismatches due to case sensitivity
        return pending.get_processed_list()
    elif source.lower() == "all":               #.lower() to avoid mismatches due to case sensitivity
        return pending.get_internal_list(), pending.get_processed_list()
    else:
        raise HTTPException(status_code=404, detail="Unknown transaction source. No list to return.")