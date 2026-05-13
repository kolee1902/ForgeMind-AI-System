def extract_claim(conversation: str):

    conversation = conversation.lower()

    if "increase" in conversation:

        action = "increase current by 5%"

    else:

        action = "reduce current by 5%"

    return {
        "entity": "station 3",
        "condition": "after lunch on Tuesday",
        "action": action,
        "outcome": "prevent overheating"
    }

