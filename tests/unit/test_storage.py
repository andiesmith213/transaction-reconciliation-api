'''
Tests storage mechanism for both pending and matched transactions
'''

def test_pending_storage(pending_tx_factory, pending_storage):
    #Generate transactions
    tx1 = pending_tx_factory(tx_id = 42, 
                             amount = 115, 
                             timestamp = 78)
    tx2 = pending_tx_factory(tx_id = 5, 
                             amount = 1000, 
                             timestamp = 80)
    tx3 = pending_tx_factory(tx_id = 112, 
                             amount = 90, 
                             timestamp = 1115)
    
    #Store into memory
    pending_storage.set_processed_transaction(tx1)
    pending_storage.set_processed_transaction(tx2)
    pending_storage.set_processed_transaction(tx3)

    pending_storage.set_internal_transaction(tx1)
    pending_storage.set_internal_transaction(tx2)
    pending_storage.set_internal_transaction(tx3)

    #Start of tests
    #1. Check list methods
    assert pending_storage.get_processed_list() == [tx1, tx2, tx3]
    assert pending_storage.get_internal_list() == [tx1, tx2, tx3]

    #2. Check valid transaction retrival
    assert pending_storage.get_processed_transaction(42) == tx1
    assert pending_storage.get_processed_list() == [tx2, tx3]

    assert pending_storage.get_internal_transaction(42) == tx1
    assert pending_storage.get_internal_list() == [tx2, tx3]

    assert pending_storage.get_processed_transaction(112) == tx3
    assert pending_storage.get_processed_list() == [tx2]
    
    assert pending_storage.get_internal_transaction(112) == tx3
    assert pending_storage.get_internal_list() == [tx2]

    #3. Check invalid transaction retrival
    assert pending_storage.get_processed_transaction(12) == None
    assert pending_storage.get_processed_list() == [tx2]
    assert pending_storage.get_processed_transaction(112) == None
    assert pending_storage.get_processed_list() == [tx2]
    
    assert pending_storage.get_internal_transaction(12) == None
    assert pending_storage.get_internal_list() == [tx2]    
    assert pending_storage.get_internal_transaction(112) == None
    assert pending_storage.get_internal_list() == [tx2]

def test_matching_storage(matching_tx_factory, matching_storage):
    #Generate transactions
    tx1 = matching_tx_factory(tx_id = 15, 
                              internal_amount = 10.0, 
                              processed_amount = 11.0,
                              internal_timestamp = 1000.0,
                              processed_timestamp = 1005.0,
                              validated = False,
                              issues = None)
    
    #Store into memory
    matching_storage.set_transaction(tx1)
    
    #Start of tests
    #1. Checking timestamp and amount methods
    assert matching_storage.get_internal_timestamp(15) == tx1.internal.timestamp
    assert matching_storage.get_processed_timestamp(15) == tx1.processed.timestamp

    assert matching_storage.get_internal_amount(15) == tx1.internal.amount
    assert matching_storage.get_processed_amount(15) == tx1.processed.amount
    
    #2. Logging issues 
    issue1 = {"status": "timestamp OOT", "details": "Tolerance exceeded"}
    issue2 = {"status": "amount OOT", "details": "Tolerance exceeded"}

    matching_storage.log_issue(15, issue1)
    assert matching_storage.get_issue_log(15) == [issue1]
    
    matching_storage.log_issue(15, issue2)
    assert matching_storage.get_issue_log(15) == [issue1, issue2]