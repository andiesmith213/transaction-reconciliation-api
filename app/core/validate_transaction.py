'''
validate_transaction.py will compare timestamp and transaction amount against a 
defined tolerance and will log errors in matched list
'''
from storage.storage import matched

def convert_to_seconds(minutes):
    return 60 * minutes

def validate_timestamp(id, tolerance):
    #Grab internal and processed timestamps
    internal_ts, processed_ts = matched.get_timestamps(id)
    #Compare against tolerance
    delta_ts = abs(internal_ts - processed_ts)
    tolerance_seconds = convert_to_seconds(tolerance)
    in_tolerance = delta_ts <= tolerance_seconds
    if in_tolerance is True:
        return {"status": "timestamp good"}
    else:
        issue_logging = {"status": "timestamp OOT", "details": "Tolerance exceeded by {} seconds".format((tolerance_seconds - delta_ts))}
        matched.log_issue(id, issue_logging)
        return issue_logging