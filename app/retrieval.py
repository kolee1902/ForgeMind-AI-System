from app.memory import get_all_claims, metrics

from app.memory import is_recent # them

def retrieve_knowledge(query: str):

    claims = get_all_claims()

    filtered = []

    for claim in claims:

        # if claim["status"] != "accepted":
        #     continue
        if claim["status"] != "accepted":
            continue
        if not is_recent(claim["timestamp"]):
            continue

        text = f"""
Entity: {claim['entity']}
Condition: {claim['condition']}
Action: {claim['action']}
Outcome: {claim['outcome']}
"""

        filtered.append(text)

    if filtered:
        metrics["retrieval_hits"] += 1

    return filtered

