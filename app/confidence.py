def detect_contradiction(new_claim, existing_claims):

    contradictions = []

    for claim in existing_claims:

        same_entity = (
            claim.entity == new_claim.entity
        )

        different_action = (
            claim.action != new_claim.action
        )

        if same_entity and different_action:
            contradictions.append(claim.claim_id)

    return contradictions
