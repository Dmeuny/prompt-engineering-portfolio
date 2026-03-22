import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import csv
from app.classifier import classify_v1, classify_v2, classify_v3


def evaluate_model(classify_fn, name):
    correct = 0
    total = 0
    filtered_total = 0

    with open("data/dataset.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            text = row["text"]
            true_label = row["label"]

            prediction = classify_fn(text)
            predicted_label = prediction["label"]
            confidence = prediction["confidence"]

            # Count all samples
            total += 1

            # Only evaluate high-confidence predictions
            if confidence >= 0.7:
                filtered_total += 1

                if predicted_label == true_label:
                    correct += 1

    accuracy = correct / filtered_total if filtered_total > 0 else 0

    print(f"{name} Accuracy (high confidence only): {accuracy:.2f}")
    print(f"{name} Coverage: {filtered_total}/{total}")
    print("-" * 40)


def run_experiment():
    evaluate_model(classify_v1, "V1")
    evaluate_model(classify_v2, "V2")
    evaluate_model(classify_v3, "V3")


if __name__ == "__main__":
    run_experiment()