from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data (you can expand later)
data = [
    ("fever and chills", "Malaria"),
    ("high temperature body pain", "Malaria"),
    ("headache and migraine", "Headache"),
    ("sharp head pain", "Headache"),
    ("cough and sore throat", "Flu"),
    ("cold and catarrh", "Flu"),
    ("stomach pain and diarrhea", "Food Poisoning"),
    ("vomiting and nausea", "Food Poisoning"),
]

texts = [d[0] for d in data]
labels = [d[1] for d in data]

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

def predict_disease(symptom_text):
    X_input = vectorizer.transform([symptom_text])
    prediction = model.predict(X_input)[0]
    return prediction
