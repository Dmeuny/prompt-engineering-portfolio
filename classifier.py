def classify_v1(text):
    text_lower = text.lower()

    if "charged" in text_lower:
        return {"label": "billing_issue", "confidence": 0.8}
    elif "crash" in text_lower:
        return {"label": "technical_issue", "confidence": 0.8}
    else:
        return {"label": "other", "confidence": 0.6}


def classify_v2(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["charged", "payment", "refund"]):
        return {"label": "billing_issue", "confidence": 0.85}
    elif any(word in text_lower for word in ["crash", "error", "slow"]):
        return {"label": "technical_issue", "confidence": 0.85}
    elif "add" in text_lower:
        return {"label": "feature_request", "confidence": 0.75}
    else:
        return {"label": "other", "confidence": 0.6}


def classify_v3(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["charged", "payment", "refund", "bill"]):
        return {"label": "billing_issue", "confidence": 0.9}

    elif any(word in text_lower for word in ["crash", "error", "bug", "slow"]):
        return {"label": "technical_issue", "confidence": 0.88}

    elif any(word in text_lower for word in ["add", "feature", "improve"]):
        return {"label": "feature_request", "confidence": 0.8}

    elif any(word in text_lower for word in ["login", "password", "account", "locked"]):
        return {"label": "account_access", "confidence": 0.85}

    else:
        return {"label": "other", "confidence": 0.6}