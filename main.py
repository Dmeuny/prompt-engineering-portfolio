from classifier import classify_v3 as classify
from router import route

text = "I was charged twice for my subscription"

result = classify(text)
destination = route(result)

print("Input:", text)
print("Classification:", result)
print("Routed to:", destination)
