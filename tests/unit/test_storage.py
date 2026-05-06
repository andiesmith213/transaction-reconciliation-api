'''
Tests storage mechanism for both pending and matched transactions
'''

def test_pending_storage(pending_tx_factory, pending_storage):
    #Generate transactions
    tx1 = pending_tx_factory(tx_id = 42, amount = 115, timestamp = 78)
    tx2 = pending_tx_factory(tx_id = 5, amount = 1000, timestamp = 80)
    tx3 = pending_tx_factory(tx_id = 112, amount = 90, timestamp = 1115)
    
    #Store
    pending_storage.set_processed_transaction(tx1)
    pending_storage.set_processed_transaction(tx2)
    pending_storage.set_processed_transaction(tx3)

    pending_storage.set_internal_transaction(tx1)
    pending_storage.set_internal_transaction(tx2)
    pending_storage.set_internal_transaction(tx3)

    #Check lists
    assert pending_storage.get_processed_list() == [tx1, tx2, tx3]
    assert pending_storage.get_internal_list() == [tx1, tx2, tx3]

    #Check valid transaction retrival
    assert pending_storage.get_processed_transaction(42) == tx1
    assert pending_storage.get_processed_list() == [tx2, tx3]

    assert pending_storage.get_internal_transaction(42) == tx1
    assert pending_storage.get_internal_list() == [tx2, tx3]

    assert pending_storage.get_processed_transaction(112) == tx3
    assert pending_storage.get_processed_list() == [tx2]
    
    assert pending_storage.get_internal_transaction(112) == tx3
    assert pending_storage.get_internal_list() == [tx2]

    #Check invalid transaction retrival
    assert pending_storage.get_processed_transaction(12) == None
    assert pending_storage.get_processed_list() == [tx2]
    
    assert pending_storage.get_internal_transaction(112) == None
    assert pending_storage.get_internal_list() == [tx2]