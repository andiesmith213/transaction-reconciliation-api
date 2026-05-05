'''
This file will store the pydantic models that will be used for this project.
FastAPI provides built-in support for pydantic. Utilizing pydantic provides 
input data type error checking and will allow for clean error handling.
'''
from pydantic import BaseModel

class PendingTransaction(BaseModel):
    tx_id: int
    amount: float
    timestamp: float

class TransactionEvent(BaseModel):
    amount: float
    timestamp: float

class MatchedTransaction(BaseModel):
    tx_id: int
    internal:  TransactionEvent
    processed: TransactionEvent
    validated: bool
    issues: list[str]