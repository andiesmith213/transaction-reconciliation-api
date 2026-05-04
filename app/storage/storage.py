'''
storage.py contains the data structures that will be used to store the
internal transaction information (expected data) versus the processed
transaction information (actual data) as well as issues found during
matching and validating transactions. 
First revision of this project will use dictionaries as storage mechanism 
for thread safe data storage.
After API is finished, next version will introduce SQLite database instead.
'''

class PendingStorage:
    def __init__(self):
        self.processed_tx = []      #List of dictionary entries containing tx id, amount, and timestamp
        self.internal_tx  = []      #List of dictionary entries containing tx id, amount, and timestamp

    #Getter methods
    def get_processed_transaction(self, tx_id):
        return self.processed_tx.pop(tx_id)
    
    def get_internal_transaction(self, tx_id):
        return self.internal_tx.pop(tx_id)
    
    #Setter methods
    def set_processed_transaction(self, transaction):
        self.processed_tx.append(transaction)
        return "Transaction {transaction.tx_id} added to pending processed transactions"
    
    def set_internal_transaction(self, transaction):
        self.internal_tx.append(transaction)
        return "Transaction {transaction.tx_id} added to pending internal transactions"
    

class MatchedStorage:
    def __init__(self):
        self.tx = []              #List of dictionary entries that will include tx id, validated flag and issue logging

pending = PendingStorage()
matched = MatchedStorage()