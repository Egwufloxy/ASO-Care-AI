def analyze_symptoms(symptoms):
    text = " ".join(symptoms).lower()

    # Smarter keyword groups
    conditions = [
        {
            "keywords": ["fever", "high temperature", "hot body", "chills"],
            "condition": "Possible Malaria or Infection",
            "advice": "Rest, stay hydrated, and consider malaria test if symptoms persist."
        },
        {
            "keywords": ["headache", "head pain", "migraine"],
            "condition": "Headache / Migraine",
            "advice": "Rest in a dark room and reduce screen time."
        },
        {
            "keywords": ["cough", "sore throat", "catarrh", "cold"],
            "condition": "Respiratory Infection",
            "advice": "Drink warm fluids and monitor symptoms."
        },
        {
            "keywords": ["stomach", "diarrhea", "vomit", "nausea"],
            "condition": "Stomach Infection",
            "advice": "Stay hydrated and avoid solid heavy food."
        }
    ]

    results = []
    score = 0

    for c in conditions:
        if any(k in text for k in c["keywords"]):
            results.append({
                "condition": c["condition"],
                "advice": c["advice"]
            })
            score += 2

    return results, score
