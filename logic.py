from ml_model import predict_disease

def analyze_symptoms(symptoms):
    text = " ".join(symptoms).lower()

    prediction = predict_disease(text)

    # Simple mapping for advice
    advice_map = {
        "Malaria": "Rest, hydrate, and get a malaria test.",
        "Headache": "Reduce stress and rest in a quiet room.",
        "Flu": "Drink warm fluids and rest.",
        "Food Poisoning": "Stay hydrated and avoid solid food temporarily."
    }

    results = [{
        "condition": prediction,
        "advice": advice_map.get(prediction, "Consult a doctor for proper diagnosis.")
    }]

    # simple severity scoring
    score_map = {
        "Malaria": 5,
        "Food Poisoning": 4,
        "Flu": 3,
        "Headache": 2
    }

    score = score_map.get(prediction, 1)

    return results, score
