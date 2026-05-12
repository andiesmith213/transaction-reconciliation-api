'''
Performs the following functions: 
- adding pending transactions to the proper list
- returning list of pending transactions
'''
from    app.storage.storage import pending
import  datetime as dt

def add_tx(transaction, src):
    source = src.lower()                                    #.lower() to avoid mismatches due to case sensitivity
    #Grab timestamp to add to transaction
    transaction.event.timestamp = dt.datetime.now().timestamp()
    #Determine source of transaction and add to appropriate pending list
    if source == "internal":           
        pending.set_internal_transaction(transaction)
        status = {"status": "added", "ID": transaction.tx_id, "source": source}
    elif source == "processed":        
        pending.set_processed_transaction(transaction)    
        status = {"status": "added", "ID": transaction.tx_id, "source": source}
    else:
        status = {"status": "error", "details": "Unknown source"}
    return status
    
def get_tx(tx_id, src):
    source = src.lower()                                    #.lower() to avoid mismatches due to case sensitivity
    #Return appropriate list based off source
    if source == "internal":            
        status = {"status": "returned", "transaction": pending.get_internal_transaction(tx_id)}
    elif source == "processed":         
        status = {"status": "returned", "transaction": pending.get_processed_transaction(tx_id)}
    elif source == "all":              
        status = {"status": "returned", "transaction": {"internal": pending.get_internal_transaction(tx_id), "processed": pending.get_processed_transaction(tx_id)}}
    else:
        status = {"status": "error", "details": "Unknown source"}
    return status

def get_tx_list(src):
    source = src.lower()                                    #.lower() to avoid mismatches due to case sensitivity
    #Return appropriate list based off source
    if source == "internal":            
        status = {"status": "returned", "list": pending.get_internal_list()}
    elif source == "processed":         
        status = {"status": "returned", "list": pending.get_processed_list()}
    elif source == "all":              
        status = {"status": "returned", "list": {"internal": pending.get_internal_list(), "processed": pending.get_processed_list()}}
    else:
        status = {"status": "error", "details": "Unknown source"}
    return status


def delete_pending_tx(tx_id, source):
    src = source.lower()
    if src == "all":
        int_tx = pending.get_internal_transaction(tx_id)
        proc_tx = pending.get_processed_transaction(tx_id)
        if int_tx is None and proc_tx is None:
            status = {"status": "no transaction to remove"}
        elif int_tx is None:
            status = {"status": "transaction removed successfully", "details": "transaction removed from processed pending transactions"}
        elif proc_tx is None:
            status = {"status": "transaction removed successfully", "details": "transaction removed from internal pending transactions"}
        else:
            status = {"status": "transaction removed successfully", "details": "transaction removed from all pending transactions"}
    elif src == "processed":
        proc_tx = pending.get_processed_transaction(tx_id)
        if proc_tx is None:
            status = {"status": "no transaction to remove"}
        else:
            status = {"status": "transaction removed successfully", "details": "transaction removed from processed pending transactions"}
    elif src == "internal":
        int_tx = pending.get_internal_transaction(tx_id)
        if int_tx is None:
            status = {"status": "no transaction to remove"}
        else:
            status = {"status": "transaction removed successfully", "details": "transaction removed from internal pending transactions"}
    return status