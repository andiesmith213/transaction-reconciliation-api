

from app.services.service_transaction import delete_pending_tx

def set_tx(src, pending_tx, pending_storage):
    if src == "all":
        pending_storage.set_internal_transaction(pending_tx)
        pending_storage.set_processed_transaction(pending_tx)
    elif src == "internal":
        pending_storage.set_internal_transaction(pending_tx)
    elif src == "processed":
        pending_storage.set_processed_transaction(pending_tx)

def test_valid_delete(pending_tx_factory, pending_storage):
    pending_tx = pending_tx_factory(tx_id = 119089)  
    #All
    src = "all"
    set_tx(src, pending_tx, pending_storage)
    delete = delete_pending_tx(pending_tx.tx_id, src)
    assert delete == {"status": "transaction removed successfully", "details": "transaction removed from all pending transactions"}
    
    #Internal
    src = "internal"
    set_tx(src, pending_tx, pending_storage)
    delete = delete_pending_tx(pending_tx.tx_id, src)
    assert delete == {"status": "transaction removed successfully", "details": "transaction removed from internal pending transactions"}
    
    #Processed
    src = "processed"
    set_tx(src, pending_tx, pending_storage)
    delete = delete_pending_tx(pending_tx.tx_id, src)
    assert delete == {"status": "transaction removed successfully", "details": "transaction removed from processed pending transactions"}

def test_invalid_delete(pending_tx_factory, pending_storage):
    pending_tx = pending_tx_factory(tx_id = 119089)  
    #All
    src = "all"
    delete = delete_pending_tx(pending_tx.tx_id, src)
    assert delete == {"status": "no transaction to remove"}
    
    #Internal
    src = "internal"
    set_tx(src, pending_tx, pending_storage)
    delete = delete_pending_tx(pending_tx.tx_id, "processed")
    assert delete == {"status": "no transaction to remove"}
    assert pending_storage.get_internal_transaction(pending_tx.tx_id) == pending_tx
    
    #Processed
    src = "processed"
    set_tx(src, pending_tx, pending_storage)
    delete = delete_pending_tx(pending_tx.tx_id, "internal")
    assert delete == {"status": "no transaction to remove"}
    assert pending_storage.get_processed_transaction(pending_tx.tx_id) == pending_tx

