'''
Pytest factory to build pseudo transactions for testing purposes
'''
import pytest
from app.models.schemas             import TransactionEvent, MatchedTransaction, PendingTransaction


@pytest.fixture
def event_factory():
    def _build(
        amount: float = 10.0,
        timestamp: float = 1000.0,
    ):
        return TransactionEvent(
            amount=amount,
            timestamp=timestamp,
        )
    return _build

@pytest.fixture
def pending_storage():
    from app.storage.storage import pending
    return pending

@pytest.fixture
def pending_tx_factory(event_factory):
    def _build(
        tx_id: int = 1,
        amount: float = 10.0,
        timestamp: float = 0.0
    ):
        return PendingTransaction(
            tx_id = tx_id,
            event = event_factory(
                amount = amount,
                timestamp = timestamp
            )
        )
    return _build

# def transaction_factory():
#     def _build(
#         tx_id: int = 1,
#         internal_amount: float = 10.0,
#         processed_amount: float = 10.0,
#         internal_timestamp: float = 1000.0,
#         processed_timestamp: float = 1000.0,
#         validated: bool = False,
#         issues: list[str] | None = None,
#     ):
#         if issues is None:
#             issues = []

#         internal = TransactionEvent(
#             amount=internal_amount,
#             timestamp=internal_timestamp,
#         )

#         processed = TransactionEvent(
#             amount=processed_amount,
#             timestamp=processed_timestamp,
#         )

#         return MatchedTransaction(
#             tx_id=tx_id,
#             internal=internal,
#             processed=processed,
#             validated=validated,
#             issues=issues,
#         )

#     return _build

# def build_matching_transaction(pass_nFail = True, time_tolerance = 10, amount_tolerance = 2):
#     #Randomize values
#     id = random.randint(0, 1000)
#     #Randomize transaction amounts based off tolerance
#     internal_amount  = random.randrange(amount_tolerance + 1, amount_tolerance + 3000)
#     processed_time   = dt.datetime.now().timestamp()
#     #if transaction should be built to pass
#     if pass_nFail is True:
#         #Build these within the tolerance range
#         processed_amount = random.randrange(internal_amount - amount_tolerance, internal_amount + amount_tolerance)
#         internal_time    = random.randrange(processed_time - time_tolerance, processed_time + time_tolerance)
#     #if transaction should be built to fail
#     else:
#         #Build these outside the tolerance range
#         below_amount = random.randrange(0, internal_amount - amount_tolerance)
#         above_amount = random.randrange(internal_amount + amount_tolerance + 1, internal_amount + amount_tolerance + 100)
#         processed_amount = random.choice(below_amount, above_amount)
#         below_time = random.randrange(processed_time - time_tolerance - 10, processed_time - time_tolerance)
#         above_time = random.randrange(processed_time + time_tolerance + 1, processed_time + time_tolerance + 100)
#         internal_time    = random.choice(below_time, above_time)

#     #Add randomized variables into proper structure
#     full_transaction = MatchedTransaction(tx_id = id,
#                                           internal = TransactionEvent(amount = internal_amount, 
#                                                                       timestamp = internal_time),
#                                           processed = TransactionEvent(amount = processed_amount, 
#                                                                        timestamp = processed_time),
#                                           validated = False,
#                                           issues = [])
#     #Store in matched memory class
#     matched.set_transaction(full_transaction)

#     return id, amount_tolerance, time_tolerance