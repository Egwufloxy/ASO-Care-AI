from logic import analyze_symptoms

user_input = input("Enter your symptoms: ")
symptoms = [user_input.lower()]

results, score = analyze_symptoms(symptoms)

if results:
    print("\n🩺 Possible Conditions:\n")

    for r in results:
        print(f"Condition: {r['condition']}")
        print(f"Advice: {r['advice']}\n")

    print("🔎 Severity Level:")

    if score >= 5:
        print("HIGH - Seek medical attention immediately")
    elif score >= 3:
        print("MEDIUM - Monitor symptoms closely")
    else:
        print("LOW - Basic care should be enough")

else:
    print("No matching symptoms found. Please consult a doctor.")
    