'''
Responsible for deleting pending transactions, getting transaction logs, etc.
'''

from app.storage.storage    import matched

def get_issue_log(tx_id):
    return matched.get_issue_log(tx_id)