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

@pytest.fixture
def matching_tx_factory():
    def _build(
        tx_id: int = 1,
        internal_amount: float = 10.0,
        processed_amount: float = 10.0,
        internal_timestamp: float = 1000.0,
        processed_timestamp: float = 1000.0,
        validated: bool = False,
        issues: list[dict] | None = None,
    ):
        if issues is None:
            issues = []

        internal = TransactionEvent(
            amount=internal_amount,
            timestamp=internal_timestamp,
        )

        processed = TransactionEvent(
            amount=processed_amount,
            timestamp=processed_timestamp,
        )

        return MatchedTransaction(
            tx_id=tx_id,
            internal=internal,
            processed=processed,
            validated=validated,
            issues=issues,
        )

    return _build

@pytest.fixture
def pending_storage():
    from app.storage.storage import pending
    return pending

@pytest.fixture
def matching_storage():
    from app.storage.storage import matched
    return matched