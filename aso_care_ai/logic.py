import json

def load_data():
    with open("aso_care_ai/data.json") as f:
        return json.load(f)

def analyze_symptoms(user_input):
    db = load_data()
    results = []
    severity_score = 0

    text = " ".join(user_input)

    for symptom in db:
        if symptom in text:
            data = db[symptom]
            results.append(data)

            if data["severity"] == "high":
                severity_score += 3
            elif data["severity"] == "medium":
                severity_score += 2
            else:
                severity_score += 1

    return results, severity_score