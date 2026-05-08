

from app.services.reconcile_transaction import reconcile_tx

import pytest

def test_valid_reconciliation(pending_tx_factory, matching_tx_factory, 
                                 pending_storage, matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115)  
    pending_storage.set_internal_transaction(pending_tx1)
    pending_storage.set_processed_transaction(pending_tx1)

    #Create expected match transactions
    matched_tx1 = matching_tx_factory(tx_id = pending_tx1.tx_id,
                                      internal_amount = pending_tx1.event.amount,
                                      internal_timestamp = pending_tx1.event.timestamp,
                                      processed_amount = pending_tx1.event.amount,
                                      processed_timestamp = pending_tx1.event.timestamp,
                                      validated = True, 
                                      issues = None
                                      )

    #Execution:
    #Call reconcile_tx function
    reconcile = reconcile_tx(42, 5, 1)
    assert reconcile == {"status": "transaction reconciled", "details": "no issues found"}
    #Check match storage against expected match
    assert matching_storage.tx[42] == matched_tx1

def test_invalid_reconciliation(matching_storage):
    #Call reconcile function without anything in pending storage
    reconcile = reconcile_tx(42, 5, 1)
    assert reconcile["status"] == "transactions not found"
    #Check matched storage does not contain transaction
    with pytest.raises(KeyError):
        matching_storage.tx[42]

def test_valid_reconciliation_timestamp_OOT(pending_tx_factory, matching_tx_factory, 
                                            pending_storage, matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115, timestamp = 50000)  
    pending_tx2 = pending_tx_factory(tx_id = 42, amount = 115, timestamp = 50)  
    pending_storage.set_internal_transaction(pending_tx1)
    pending_storage.set_processed_transaction(pending_tx2)

    #Create expected match transactions
    OOT_range = float((abs(50000 - 50)) - (5 * 60))
    issue_log = [{"status": "timestamp OOT", "details": "Tolerance exceeded by {} seconds".format((OOT_range))}]
    matched_tx1 = matching_tx_factory(tx_id = pending_tx1.tx_id,
                                      internal_amount = pending_tx1.event.amount,
                                      internal_timestamp = pending_tx1.event.timestamp,
                                      processed_amount = pending_tx2.event.amount,
                                      processed_timestamp = pending_tx2.event.timestamp,
                                      validated = True, 
                                      issues = issue_log
                                      )

    #Execution:
    #Call reconcile_tx function
    reconcile = reconcile_tx(42, 5, 1)
    assert reconcile == {"status": "transaction reconciled", "details": "issues found, see log for details"}
    #Check match storage against expected match
    assert matching_storage.tx[42] == matched_tx1

def test_valid_reconciliation_amount_OOT(pending_tx_factory, matching_tx_factory, 
                                         pending_storage, matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115, timestamp = 50000)  
    pending_tx2 = pending_tx_factory(tx_id = 42, amount = 120, timestamp = 50000)  
    pending_storage.set_internal_transaction(pending_tx1)
    pending_storage.set_processed_transaction(pending_tx2)

    #Create expected match transactions
    OOT_range = float((abs(115 - 120)) - 1)
    issue_log = [{"status": "amount OOT", "details": "Tolerance exceeded by ${}".format((OOT_range))}]
    matched_tx1 = matching_tx_factory(tx_id = pending_tx1.tx_id,
                                      internal_amount = pending_tx1.event.amount,
                                      internal_timestamp = pending_tx1.event.timestamp,
                                      processed_amount = pending_tx2.event.amount,
                                      processed_timestamp = pending_tx2.event.timestamp,
                                      validated = True, 
                                      issues = issue_log
                                      )

    #Execution:
    #Call reconcile_tx function
    reconcile = reconcile_tx(42, 5, 1)
    assert reconcile == {"status": "transaction reconciled", "details": "issues found, see log for details"}
    #Check match storage against expected match
    assert matching_storage.tx[42] == matched_tx1

def test_valid_reconciliation_both_OOT(pending_tx_factory, matching_tx_factory, 
                                       pending_storage, matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115, timestamp = 50)  
    pending_tx2 = pending_tx_factory(tx_id = 42, amount = 120, timestamp = 50000)  
    pending_storage.set_internal_transaction(pending_tx1)
    pending_storage.set_processed_transaction(pending_tx2)

    #Create expected match transactions
    OOT_ts_range = float((abs(50 - 50000)) - (5 * 60))
    OOT_amt_range = float((abs(115 - 120)) - 1)
    issue_log = [{"status": "timestamp OOT", "details": "Tolerance exceeded by {} seconds".format((OOT_ts_range))},
                 {"status": "amount OOT", "details": "Tolerance exceeded by ${}".format((OOT_amt_range))}]
    matched_tx1 = matching_tx_factory(tx_id = pending_tx1.tx_id,
                                      internal_amount = pending_tx1.event.amount,
                                      internal_timestamp = pending_tx1.event.timestamp,
                                      processed_amount = pending_tx2.event.amount,
                                      processed_timestamp = pending_tx2.event.timestamp,
                                      validated = True, 
                                      issues = issue_log
                                      )

    #Execution:
    #Call reconcile_tx function
    reconcile = reconcile_tx(42, 5, 1)
    assert reconcile == {"status": "transaction reconciled", "details": "issues found, see log for details"}
    #Check match storage against expected match
    assert matching_storage.tx[42] == matched_tx1