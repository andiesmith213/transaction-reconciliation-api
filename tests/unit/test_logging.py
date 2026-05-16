
from app.services.report_transaction import get_issue_log

def test_issue_log_occupied(matching_tx_factory, matching_storage):    
    issue_log1 = [{"status": "timestamp OOT", "details": "Tolerance exceeded"},
                 {"status": "amount OOT", "details": "Tolerance exceeded"}]
    issue_log2 = [{"status": "timestamp OOT", "details": "Tolerance exceeded"}]
    issue_log3 = [{"status": "amount OOT", "details": "Tolerance exceeded"}]
    tx1 = matching_tx_factory(tx_id = 112,
                              internal_amount = 70,
                              internal_timestamp = 10,
                              processed_amount = 70,
                              processed_timestamp = 11,
                              validated = True, 
                              issues = issue_log1
                              )
    tx2 = matching_tx_factory(tx_id = 18,
                              internal_amount = 70,
                              internal_timestamp = 10,
                              processed_amount = 70,
                              processed_timestamp = 11,
                              validated = True, 
                              issues = issue_log2
                              )
    tx3 = matching_tx_factory(tx_id = 1523418,
                              internal_amount = 70,
                              internal_timestamp = 10,
                              processed_amount = 70,
                              processed_timestamp = 11,
                              validated = True, 
                              issues = issue_log3
                              )
    matching_storage.set_transaction(tx1)
    matching_storage.set_transaction(tx2)
    matching_storage.set_transaction(tx3)
    assert get_issue_log(112)       == issue_log1
    assert get_issue_log(18)        == issue_log2
    assert get_issue_log(1523418)   == issue_log3   

def test_issue_log_empty(matching_tx_factory, matching_storage):    
    issue_log1 = []
    tx1 = matching_tx_factory(tx_id = 112,
                              internal_amount = 70,
                              internal_timestamp = 10,
                              processed_amount = 70,
                              processed_timestamp = 11,
                              validated = True, 
                              issues = issue_log1
                              )
    matching_storage.set_transaction(tx1)
    assert get_issue_log(112) == {"status": "not found", "details": "no issue log found"}

def test_log_when_tx_not_validated(matching_tx_factory, matching_storage):    
    issue_log1 = []
    tx1 = matching_tx_factory(tx_id = 112,
                              internal_amount = 70,
                              internal_timestamp = 10,
                              processed_amount = 70,
                              processed_timestamp = 11,
                              validated = False, 
                              issues = issue_log1
                              )
    matching_storage.set_transaction(tx1)
    assert get_issue_log(112) == {"status": "error", "details": "transaction not validated"}

def test_log_matched_missing():    
    assert get_issue_log(112) == {"status": "error", "details": "transaction ID does not exist"}