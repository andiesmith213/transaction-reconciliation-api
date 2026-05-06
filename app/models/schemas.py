'''
This file will store the pydantic models that will be used for this project.
FastAPI provides built-in support for pydantic. Utilizing pydantic provides 
input data type error checking and will allow for clean error handling.
'''
from pydantic import BaseModel

class TransactionEvent(BaseModel):
    amount: float
    timestamp: float

class PendingTransaction(BaseModel):
    tx_id: int
    event: TransactionEvent

class MatchedTransaction(BaseModel):
    tx_id: int
    internal:  TransactionEvent
    processed: TransactionEvent
    validated: bool
    issues: list[dict]