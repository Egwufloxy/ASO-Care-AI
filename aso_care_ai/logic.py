from ml_model import predict_disease

def analyze_symptoms(symptoms: str):
    """
    Convert user symptoms into ML prediction
    """

    if not symptoms:
        return "Please enter symptoms"

    symptoms = symptoms.lower().strip()

    # call model
    prediction = predict_disease([symptoms])

    if prediction:
        return prediction[0]
    else:
        return "No matching condition found. Please consult a doctor."