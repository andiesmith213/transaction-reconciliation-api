'''
reconcile_transaction.py contains functions to both match and validate
transactions that it recieves from the router. It will return a message
providing the router with details on the transaction and any issues found.
'''
from app.core.match_transaction     import match_events
from app.core.validate_transaction  import validate_timestamp, validate_amount
from app.storage.storage            import matched

#Wrapper function that will call match and validate functions.
#Handles higher level passing of information
def reconcile_tx(tx_id, time_tolerance, amount_tolerance):
    #Match processed and internal transactions
    match = match_events(tx_id)
    #Check for error state
    if match["status"] == "transaction matched":
        #Validate timestamp
        ts = validate_timestamp(tx_id, time_tolerance)
        #Validate amount
        amt = validate_amount(tx_id, amount_tolerance)
        matched.set_validated_true(tx_id)
        if (ts["status"] == "timestamp good") and (amt["status"] == "amount good"):
            return {"status": "transaction reconciled", "details": "no issues found"}
        else:
            return {"status": "transaction reconciled", "details": "issues found, see log for details"}
    else:
        return match