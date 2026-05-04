'''
handle_transaction.py performs the following: 
- adding pending transactions to the proper list
- returning list of pending transactions
'''
from storage.storage import pending

def add_tx(transaction):
    #Determine source of transaction and add to appropriate pending list
    if transaction.source.lower() == "internal":            #.lower() to avoid mismatches due to case sensitivity
        pending.set_internal_transaction(transaction)
    elif transaction.source.lower() == "processed":         #.lower() to avoid mismatches due to case sensitivity
        pending.set_processed_transaction(transaction)    
    return {"status": "added", "ID": transaction.tx_id, "source": transaction.source}
    
def get_tx(source):
    #Return appropriate list based off source
    if source.lower() == "internal":            
        return pending.get_internal_list()
    elif source.lower() == "processed":         #.lower() to avoid mismatches due to case sensitivity
        return pending.get_processed_list()
    elif source.lower() == "all":               #.lower() to avoid mismatches due to case sensitivity
        return pending.get_internal_list(), pending.get_processed_list()