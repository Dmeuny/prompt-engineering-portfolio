# prompt-engineering

# 🧠 LLM Classification & Prompt Optimization System

## 📌 Overview

This project simulates an AI system that classifies and routes customer support tickets.

For example, if a customer says “I was charged twice,” the system classifies it as Billing and routes it to the correct team, reducing manual triage and improving response efficiency.

The goal is to move beyond one-off prompting and show how prompts can be designed, tested, and improved as part of a larger system.

It highlights prompt engineering, classification design, evaluation, and A/B testing strategies aligned with real-world AI systems.

---

## 🚀 Problem

Businesses receive large volumes of unstructured user messages (support tickets, chats, emails). These must be:

* Accurately classified
* Routed to the correct team
* Handled with minimal manual intervention

---

## 🏗️ System Architecture

**Pipeline:**

1. Input text
2. Classification model
3. Confidence scoring
4. Routing decision
5. Evaluation & monitoring

---

## 🧪 Classification Models

Three versions were implemented to simulate prompt iteration:

* **V1 (Baseline):** Minimal keyword matching
* **V2 (Improved):** Expanded keyword coverage
* **V3 (Optimized):** Structured logic with better category separation

---

## 📊 Evaluation Results

### Overall Accuracy

| Model | Accuracy |
| ----- | -------- |
| V1    | 0.33     |
| V2    | 0.73     |
| V3    | 0.93     |

---

### High-Confidence Performance (≥ 0.7)

| Model | Accuracy | Coverage |
| ----- | -------- | -------- |
| V1    | 1.00     | 2/15     |
| V2    | 1.00     | 8/15     |
| V3    | 1.00     | 11/15    |

---

## 🧠 Key Insights

* Increasing classification specificity significantly improves performance
* Accuracy alone is not sufficient — **coverage is critical in production systems**
* Confidence thresholds help balance **precision vs. automation**

---

## ⚖️ Tradeoffs

* Higher accuracy models may reduce coverage if overly strict
* Simpler models are easier to maintain but less reliable
* Production systems require balancing:

  * Accuracy
  * Coverage
  * Complexity

---

## 🧭 Routing Logic

Based on classification output:

* `billing_issue` → Billing queue
* `technical_issue` → Tech support
* `feature_request` → Product team
* `account_access` → Account support
* Low confidence → Human review

---

## 🛠️ Tech Stack

* Python
* CSV dataset
* Rule-based classifier (LLM simulation)
* Modular architecture (classifier, router, evaluation)

---

## 🔮 Future Improvements

* Replace rule-based classifier with real LLM (OpenAI API)
* Add confusion matrix and deeper metrics
* Implement real-time logging & monitoring
* Build API endpoint for production deployment

---

## 💡 Key Takeaway

This project demonstrates how prompt engineering is not just about writing prompts, but about:

* Iteration
* Measurement
* Tradeoff analysis
* Production readiness

---

## ▶️ How to Run

```bash
py main.py
py eval/evaluate.py
```
