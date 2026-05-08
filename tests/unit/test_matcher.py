

from app.core.match_transaction import match_events

import pytest

def test_valid_transaction_match(pending_tx_factory, matching_tx_factory, 
                                 pending_storage, matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115)
    pending_tx2 = pending_tx_factory(tx_id = 35, amount = 1105)    
    pending_storage.set_internal_transaction(pending_tx1)
    pending_storage.set_internal_transaction(pending_tx2)
    pending_storage.set_processed_transaction(pending_tx1)
    pending_storage.set_processed_transaction(pending_tx2)

    #Create expected match transactions
    matched_tx1 = matching_tx_factory(tx_id = pending_tx1.tx_id,
                                      internal_amount = pending_tx1.event.amount,
                                      internal_timestamp = pending_tx1.event.timestamp,
                                      processed_amount = pending_tx1.event.amount,
                                      processed_timestamp = pending_tx1.event.timestamp
                                      )
    matched_tx2 = matching_tx_factory(tx_id = pending_tx2.tx_id,
                                      internal_amount = pending_tx2.event.amount,
                                      internal_timestamp = pending_tx2.event.timestamp,
                                      processed_amount = pending_tx2.event.amount,
                                      processed_timestamp = pending_tx2.event.timestamp
                                      )

    #Execution:
    #Call match_events function
    match = match_events(42)
    assert match["status"] == "transaction matched"
    match = match_events(35)
    assert match["status"] == "transaction matched"
    #Check match storage against expected match
    assert matching_storage.tx[42] == matched_tx1
    assert matching_storage.tx[35] == matched_tx2
    #Check pending storage does not contain transaction
    with pytest.raises(KeyError):
        pending_storage.internal_tx[42]
        pending_storage.internal_tx[35]
        pending_storage.processed_tx[42]
        pending_storage.processed_tx[35]

def test_missing_processed_tx(pending_tx_factory,pending_storage, 
                              matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115)  
    pending_storage.set_internal_transaction(pending_tx1)

    #Execution:
    #Call match_events function
    match = match_events(42)
    assert match["status"] == "waiting for processed"
    #Check matched storage does not contain transaction
    with pytest.raises(KeyError):
        matching_storage.tx[42]
    #Check that internal transaction was placed back in pending storage
    assert pending_storage.get_internal_list() == [pending_tx1]

def test_missing_internal_tx(pending_tx_factory,pending_storage, 
                             matching_storage):
    #Setup:
    #Create pending transactions and store in pending storage
    pending_tx1 = pending_tx_factory(tx_id = 42, amount = 115)  
    pending_storage.set_processed_transaction(pending_tx1)

    #Execution:
    #Call match_events function
    match = match_events(42)
    assert match["status"] == "waiting for internal"
    #Check matched storage does not contain transaction
    with pytest.raises(KeyError):
        matching_storage.tx[42]
    #Check that internal transaction was placed back in pending storage
    assert pending_storage.get_processed_list() == [pending_tx1]

def test_both_tx_missing(matching_storage):
    #Call match_events function
    match = match_events(42)
    assert match["status"] == "transactions not found"
    #Check matched storage does not contain transaction
    with pytest.raises(KeyError):
        matching_storage.tx[42]