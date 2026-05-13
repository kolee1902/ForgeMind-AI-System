review_queue = []

worker_trust = {
    "worker_1": 0.9,
    "worker_2": 0.4,
    "worker_3": 0.7
}


knowledge_store = []


metrics = {
    "accepted_claims": 0,
    "conflicts": 0,
    "quarantined": 0,
    "retrieval_hits": 0
}
def detect_conflict(new_claim):

    for claim in knowledge_store:

        same_entity = (
            claim["entity"].lower() == new_claim.entity.lower()
        )

        different_action = (
            claim["action"].lower() != new_claim.action.lower()
        )

        if same_entity and different_action:
            return True

    return False


def store_claim(claim):

    conflict = detect_conflict(claim)

    if conflict:
        # claim.status = "conflict"
        # claim.confidence = 0.2

        # metrics["conflicts"] += 1
        # metrics["quarantined"] += 1
        claim.status = "conflict"
        claim.confidence = 0.2
        review_queue.append(claim.dict())
        metrics["conflicts"] += 1
        metrics["quarantined"] += 1

    elif claim.confidence < 0.5:
        # claim.status = "quarantined"

        # metrics["quarantined"] += 1
        claim.status = "quarantined"
        review_queue.append(claim.dict())
        metrics["quarantined"] += 1

    else:
        claim.status = "accepted"

        metrics["accepted_claims"] += 1

    knowledge_store.append({
        "id": claim.claim_id,
        "entity": claim.entity,
        "condition": claim.condition,
        "action": claim.action,
        "outcome": claim.outcome,
        "confidence": claim.confidence,
        "status": claim.status,
        "worker": claim.source_worker,
        "timestamp": claim.timestamp # them
    })


def get_all_claims():

    return knowledge_store



def get_metrics():

    return metrics

def get_worker_trust(worker_id):

    return worker_trust.get(worker_id, 0.5)

# them
from datetime import datetime
def is_recent(timestamp_str):

    claim_time = datetime.fromisoformat(timestamp_str)

    now = datetime.now()

    age_days = (now - claim_time).days

    return age_days < 30
# them
def get_review_queue():

    return review_queue
def approve_claim(claim_id):

    global review_queue

    for claim in review_queue:

        if claim["claim_id"] == claim_id:

            claim["status"] = "accepted" #

            knowledge_store[:] = [

                c for c in knowledge_store

                if not (
                    c["entity"] == claim["entity"]
                    and c["action"] != claim["action"]
                )
            ]
            knowledge_store.append(claim)#

            metrics["accepted_claims"] += 1

            review_queue = [
                c for c in review_queue
                if c["claim_id"] != claim_id
            ]

            return True

    return False
def reject_claim(claim_id):

    global review_queue

    review_queue = [
        c for c in review_queue
        if c["claim_id"] != claim_id
    ]

    return True


