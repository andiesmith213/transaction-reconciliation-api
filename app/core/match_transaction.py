'''
match_transaction.py will compare the processed and internal
transaction lists and, upon finding a match, will remove transactions
from pending queue and store them into matched list
'''
from storage.storage            import pending, matched
from models.schemas             import MatchedTransaction, TransactionEvent

def match_events(id):
    processed_event = pending.get_processed_transaction(id)
    internal_event = pending.get_internal_transaction(id)
    #If both events are not found, return not found status
    if processed_event is None and internal_event is None:
        return {"status": "transactions not found"}
    #If one event is not found, buffer and wait for other transaction
    elif processed_event is None:
        pending.set_internal_transaction(internal_event)
        return {"status": "waiting for processed"}
    elif internal_event is None:
        pending.set_processed_transaction(processed_event)
        return {"status": "waiting for internal"}
    else:
        #Once both transactions are found, configure into MatchedTransaction scheme and store in matched
        matched.set_transaction(build_matched_transaction(id, internal_event, processed_event))
        return {"status": "transaction matched"}

def build_matched_transaction(id, internal, processed):
    full_transaction = MatchedTransaction(tx_id = id,
                                          internal = TransactionEvent(amount = internal.amount, timestamp = internal.timestamp),
                                          processed = TransactionEvent(amount = processed.amount, timestamp = processed.timestamp),
                                          validated = False,
                                          issues = [])
    return full_transaction