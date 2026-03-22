def route(result):
    label = result["label"]
    confidence = result["confidence"]

    # Fallback for low confidence
    if confidence < 0.7:
        return "human_review"

    # Routing logic
    if label == "billing_issue":
        return "billing_queue"

    elif label == "technical_issue":
        return "tech_support_queue"

    elif label == "feature_request":
        return "product_team_queue"

    elif label == "account_access":
        return "account_support_queue"

    else:
        return "general_queue"