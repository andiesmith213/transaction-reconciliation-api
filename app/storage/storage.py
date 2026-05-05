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
        self.processed_tx = {}      #Dictionary entries containing tx id, amount, and timestamp
        self.internal_tx  = {}      #Dictionary entries containing tx id, amount, and timestamp
        self.processed_index = 0    #Tracks latest index value
        self.internal_index = 0     #Tracks latest index value

    #Getter methods
    def get_processed_transaction(self, tx_id):
        result = self.processed_tx.pop(tx_id, None)
        self.processed_index = len(self.processed_tx) - 1
        return result
    
    def get_internal_transaction(self, tx_id):
        result = self.internal_tx.pop(tx_id, None)
        self.internal_index = len(self.internal_tx) - 1
        return result

    def get_processed_list(self):
        return list(self.processed_tx.values())

    def get_internal_list(self):
        return list(self.internal_tx.values())
    
    #Setter methods
    def set_processed_transaction(self, transaction):
        self.processed_tx[transaction.tx_id] = transaction
        self.processed_index = len(self.processed_tx) - 1
    
    def set_internal_transaction(self, transaction):
        self.internal_tx[transaction.tx_id] = transaction
        self.internal_index = len(self.internal_tx) - 1
    

class MatchedStorage:
    def __init__(self):
        self.tx = {}              #Dictionary entries that will include tx id, amounts, timestamps, validated flag and issue logging

    def set_transaction(self, transaction):
        self.tx[transaction.tx_id] = transaction
    
    def get_transaction(self, id):
        return self.tx[id]

pending = PendingStorage()
matched = MatchedStorage()