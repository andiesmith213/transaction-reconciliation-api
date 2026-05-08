'''
validate_transaction.py will compare timestamp and transaction amount against a 
defined tolerance and will log errors in matched list
'''
from app.storage.storage import matched

def convert_to_seconds(minutes):
    return 60 * minutes

def check_tolerance(val1, val2, tolerance):
    delta = abs(val1 - val2)
    in_tolerance = delta <= tolerance
    if in_tolerance is True:
        return in_tolerance, None
    else:
        return in_tolerance, round(delta - tolerance, 2)

def validate_timestamp(id, tolerance):
    #Grab internal and processed timestamps
    internal_ts, processed_ts = matched.get_timestamps(id)
    #Compare against tolerance
    tolerance_seconds = convert_to_seconds(tolerance)   #conversion needed as timestamps are measured in seconds, tolerance will be provided in minutes
    in_tolerance, OOT = check_tolerance(internal_ts, processed_ts, tolerance_seconds)
    if in_tolerance is True:
        return {"status": "timestamp good"}
    else:
        issue_logging = {"status": "timestamp OOT", "details": "Tolerance exceeded by {} seconds".format((OOT))}
        matched.log_issue(id, issue_logging)
        return issue_logging
    
def validate_amount(id, tolerance):
    #Grab internal and processed timestamps
    internal_amt, processed_amt = matched.get_amounts(id)
    #Compare against tolerance
    in_tolerance, OOT = check_tolerance(internal_amt, processed_amt, tolerance)
    if in_tolerance is True:
        return {"status": "amount good"}
    else:
        issue_logging = {"status": "amount OOT", "details": "Tolerance exceeded by ${}".format((OOT))}
        matched.log_issue(id, issue_logging)
        return issue_logging