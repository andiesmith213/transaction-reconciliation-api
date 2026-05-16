'''
Responsible for getting transaction logs
'''

from app.storage.storage    import matched

def get_issue_log(tx_id):
    if tx_id in matched.tx:
        if matched.get_validated(tx_id) is True:
            log = matched.get_issue_log(tx_id)
            if log == []:
                return {"status": "not found", "details": "no issue log found"}
            else:
                return log
        else:
            return {"status": "error", "details": "transaction not validated"}
    else:
        return {"status": "error", "details": "transaction ID does not exist"}