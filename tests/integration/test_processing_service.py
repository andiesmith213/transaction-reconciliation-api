

from app.services.process_transaction import add_tx, get_tx

def test_valid_add_to_pending(pending_tx_factory):
    tx1 = pending_tx_factory(tx_id = 42, 
                             amount = 115)
    tx2 = pending_tx_factory(tx_id = 35, 
                             amount = 1105)
    
    internal_tx1 = add_tx(tx1, "INternal")
    assert internal_tx1["status"] == "added"
    processed_tx1 = add_tx(tx1, "processed")
    assert processed_tx1["status"] == "added"
    internal_tx2 = add_tx(tx2, "internal")
    assert internal_tx2["status"] == "added"
    processed_tx2 = add_tx(tx2, "PRoCessed")
    assert processed_tx2["status"] == "added"

    get_tx1_all = get_tx(42, "ALL")
    assert get_tx1_all["transaction"]["internal"] == tx1
    assert get_tx1_all["transaction"]["processed"] == tx1
    
    get_tx2_all = get_tx(35, "All")
    assert get_tx2_all["transaction"]["internal"] == tx2
    assert get_tx2_all["transaction"]["processed"] == tx2

def test_invalid_add_to_pending(pending_tx_factory):
    tx1 = pending_tx_factory(tx_id = 198, 
                             amount = 500)
    tx2 = pending_tx_factory(tx_id = 365, 
                             amount = 0.5)
    
    error_tx1 = add_tx(tx1, "no source")
    error_tx2 = add_tx(tx2, "no source")

    assert error_tx1["status"] == "error"
    assert error_tx2["status"] == "error"

    get_tx1_error = get_tx(198, "no source")
    get_tx2_error = get_tx(365, "no source")

    assert get_tx1_error["status"] == "error"
    assert get_tx2_error["status"] == "error"
