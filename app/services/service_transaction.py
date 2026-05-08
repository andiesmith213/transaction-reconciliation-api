'''
Responsible for deleting pending transactions, getting transaction logs, etc.
'''

from app.storage.storage    import pending, matched

def get_issue_log(tx_id):
    return matched.get_issue_log(tx_id)

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