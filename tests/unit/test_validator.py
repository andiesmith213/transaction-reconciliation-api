


from app.core.validate_transaction import validate_timestamp, validate_amount, check_tolerance

def test_check_tolerance():
    #In tolerance behavior
    in_tolerance, OOT = check_tolerance(10.5, 10, 1)
    assert in_tolerance == True
    assert OOT == None
    #Out of tolerance behavior
    in_tolerance, OOT = check_tolerance(1000, 10, 1)
    assert in_tolerance == False
    assert OOT == ((1000 - 10) - 1)
    
def test_timestamp_validation_in_tolerance(matching_tx_factory, matching_storage):
    #Setup:
    #Create expected match transaction and store in matched storage
    matched_tx1 = matching_tx_factory(tx_id = 67009,
                                      internal_timestamp = 7890,
                                      processed_timestamp = 7895
                                      )
    matching_storage.set_transaction(matched_tx1)

    #Execution:
    #Call validate_timestamp function
    valid_ts = validate_timestamp(67009, 10)
    #Check status
    assert valid_ts["status"] == "timestamp good"
    #Check that no issue was logged
    issue_log = matching_storage.get_issue_log(67009)
    assert issue_log == []

def test_timestamp_validation_out_of_tolerance(matching_tx_factory, matching_storage):
    #Setup:
    #Create expected match transaction and store in matched storage
    matched_tx1 = matching_tx_factory(tx_id = 67009,
                                      internal_timestamp = 30000,
                                      processed_timestamp = 5
                                      )
    matching_storage.set_transaction(matched_tx1)

    #Execution:
    #Call validate_timestamp function
    invalid_ts = validate_timestamp(67009, 10)
    #Check status
    assert invalid_ts["status"] == "timestamp OOT"
    #Check that issue was logged
    issue_log = matching_storage.get_issue_log(67009)
    OOT_range = float((abs(30000 - 5)) - (10 * 60))
    assert issue_log == [{"status": "timestamp OOT", "details": "Tolerance exceeded by {} seconds".format((OOT_range))}]

def test_amount_validation_in_tolerance(matching_tx_factory, matching_storage):
    #Setup:
    #Create expected match transaction and store in matched storage
    matched_tx1 = matching_tx_factory(tx_id = 9,
                                      internal_amount = 7890,
                                      processed_amount = 7890.5
                                      )
    matching_storage.set_transaction(matched_tx1)

    #Execution:
    #Call validate_amount function
    valid_amt = validate_amount(9, 0.5)  #edge case of right on boundary, should still be valid
    #Check status
    assert valid_amt["status"] == "amount good"
    #Check that no issue was logged
    issue_log = matching_storage.get_issue_log(9)
    assert issue_log == []

def test_amount_validation_out_of_tolerance(matching_tx_factory, matching_storage):
    #Setup:
    #Create expected match transaction and store in matched storage
    matched_tx1 = matching_tx_factory(tx_id = 9,
                                      internal_amount = 7990,
                                      processed_amount = 7990.55
                                      )
    matching_storage.set_transaction(matched_tx1)

    #Execution:
    #Call validate_amount function
    invalid_amt = validate_amount(9, 0.5)
    #Check status
    assert invalid_amt["status"] == "amount OOT"
    #Check that issue was logged
    issue_log = matching_storage.get_issue_log(9)
    assert issue_log == [{"status": "amount OOT", "details": "Tolerance exceeded by ${}".format((0.05))}]