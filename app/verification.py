from app.memory import get_worker_trust


def verify_claim(claim):

    trust = get_worker_trust(claim.source_worker)

    confidence = claim.confidence * trust

    claim.confidence = round(confidence, 2)

    if claim.confidence > 0.6:
        claim.status = "accepted"

    elif claim.confidence > 0.4:
        claim.status = "observed"

    else:
        claim.status = "quarantined"

    return claim

