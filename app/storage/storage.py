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
        self.processed_index = 0    #Tracks latest index value
        self.internal_index = 0     #Tracks latest index value

    #Getter methods
    def get_processed_transaction(self, tx_id):
        if self.processed_index > 0:
            self.processed_index -= 1
        return self.processed_tx.pop(tx_id)
    
    def get_internal_transaction(self, tx_id):
        if self.internal_index > 0:
            self.internal_index -= 1
        return self.internal_tx.pop(tx_id)
    
    #Setter methods
    def set_processed_transaction(self, transaction):
        self.processed_tx.append(transaction)
        self.processed_index = len(self.processed_tx) - 1
        # return self.processed_tx
    
    def set_internal_transaction(self, transaction):
        self.internal_tx.append(transaction)
        self.internal_index = len(self.internal_tx) - 1
        # return self.internal_tx
    

class MatchedStorage:
    def __init__(self):
        self.tx = []              #List of dictionary entries that will include tx id, validated flag and issue logging

pending = PendingStorage()
matched = MatchedStorage()