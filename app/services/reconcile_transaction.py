'''
reconcile_transaction.py contains functions to both match and validate
transactions that it recieves from the router. It will return a message
providing the router with details on the transaction and any issues found.
'''
from app.core.match_transaction     import match_events
from app.core.validate_transaction  import validate_timestamp

#Wrapper function that will call match and validate functions.
#Handles higher level passing of information
def reconcile_tx(tx_id, time_tolerance):
    #Match processed and internal transactions
    match_events(tx_id)
    #Validate timestamp
    validate_timestamp(tx_id, time_tolerance)