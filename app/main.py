from fastapi import FastAPI

from app.models import LearnRequest, AskRequest, OperationalClaim
from app.extraction import extract_claim
from app.verification import verify_claim
from app.memory import store_claim, get_metrics
from app.voice_agent import answer_worker

import uuid

from datetime import datetime # them
from app.memory import (
    get_metrics,
    get_review_queue,
    approve_claim,
    reject_claim
) # them


# app = FastAPI()
app = FastAPI(debug=True)


@app.post("/learn")
def learn_from_worker(request: LearnRequest):

    transcript = request.conversation

    extracted = extract_claim(transcript)

    claim = OperationalClaim(
        claim_id=str(uuid.uuid4()),
        entity=extracted["entity"],
        condition=extracted["condition"],
        action=extracted["action"],
        outcome=extracted["outcome"],
        confidence=0.7,
        source_worker=request.worker_id,
        status="observed",
        timestamp=str(datetime.now()) # them 
    )

    verified_claim = verify_claim(claim)

    store_claim(verified_claim)

    return {
        "status": verified_claim.status,
        "confidence": verified_claim.confidence
    }


@app.post("/ask")
def ask_agent(request: AskRequest):

    answer = answer_worker(request.question)

    return {
        "answer": answer
    }


@app.get("/metrics")
def metrics():

    return get_metrics()

#them
@app.get("/review_queue")
def review_queue():

    return get_review_queue()
@app.post("/approve/{claim_id}")
def approve(claim_id: str):

    success = approve_claim(claim_id)

    return {
        "approved": success
    }
@app.post("/reject/{claim_id}")
def reject(claim_id: str):

    success = reject_claim(claim_id)

    return {
        "rejected": success
    }