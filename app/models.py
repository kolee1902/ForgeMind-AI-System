from pydantic import BaseModel


class LearnRequest(BaseModel):
    conversation: str
    worker_id: str


class AskRequest(BaseModel):
    question: str


class OperationalClaim(BaseModel):

    claim_id: str

    entity: str
    condition: str
    action: str
    outcome: str

    confidence: float

    source_worker: str

    status: str

    timestamp: str

