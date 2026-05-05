'''
handle_transaction.py performs the following: 
- adding pending transactions to the proper list
- returning list of pending transactions
'''
from storage.storage import pending
import datetime as dt

def add_tx(transaction, source):
    #Grab timestamp to add to transaction
    transaction.timestamp = dt.datetime.now().timestamp()
    #Determine source of transaction and add to appropriate pending list
    if source == "internal":           
        pending.set_internal_transaction(transaction)
    elif source == "processed":        
        pending.set_processed_transaction(transaction)    
    return {"status": "added", "ID": transaction.tx_id, "source": source}
    
def get_tx(source):
    #Return appropriate list based off source
    if source == "internal":            
        return {"status": "returned", "internal list": pending.get_internal_list()}
    elif source == "processed":         
        return {"status": "returned", "processed list": pending.get_processed_list()}
    elif source == "all":              
        return {"status": "returned", "internal list": pending.get_internal_list(), "processed list": pending.get_processed_list()}