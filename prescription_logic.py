# d_1_prescription_dict: dict = {
#     "malaria": {
#         "drug": "Artenether/Lumefantrine (20/120mg)",
#         "Dosage": {
#             1/3: "1x2 for 3 days",
#             3:
#         }
#     }
# }

def prescript_d(disease: str, age: float, weight: float = 0.0) -> (str, str):
    if disease.lower() == "typhoid":
        if age > 16:
            return "Ciprofloxacin (500mg)", "1x2 for 2 weeks"
        else:
            if weight == 0.0:
                return "Weight is required for children"
            return "Ciprofloxacin (500mg)", f"{0.03 * weight}x2 for 2 weeks"

    elif disease.lower() == "common cold":
        if age > 16:
            return "Paracetamol (500mg)", "2x3 for 3 days"
        else:
            if weight == 0.0:
                return "Weight is required for children"
            return "Paracetamol (500mg)", f"{0.02 * weight}x3 for 3 days"
    elif disease.lower() == "pneumonia":
        if 0 < age < 1:
            return "Amoxicillin dispersible Tabs", "1x2 for 5 days"
        elif 1 < age < 3:
            return "Amoxicillin dispersible Tabs", "2x2 for 5 days"
        elif 3 < age < 5:
            return "Amoxicillin dispersible Tabs", "3x2 for 5 days"
        elif 5 < age < 16:
            if weight == 0.0:
                return "Weight is required for children"
            return "Amoxicillin Capsules", f"{0.08 * weight}x4 for 5days"
        else:
            return "Amoxicillin Capsules", "1x4 for 5 days"
    elif disease.lower() == "malaria":
        if weight == 0.0:
            if 5 / 12 < age < 11 / 12:
                return "Artesunate(50mg)/Amodiaquine(153mg)", "1/2x1 for 3 days"
            elif 1 < age < 6:
                return "Artesunate(50mg)/Amodiaquine(153mg)", "1x1 for 3 days"
            elif 7 < age < 13:
                return "Artesunate(50mg)/Amodiaquine(153mg)", "2x1 for 3 days"
            else:
                return "Artesunate(50mg)/Amodiaquine(153mg)", "4x1 for 3 days"
        else:
            if (1 / 3 < age < 3) and (5 < weight < 14):
                return "Artenether/Lumefantrine (20/120mg)", "1x2 for 3 days"
            elif (3 < age < 12) and (15 < weight < 24):
                return "Artenether/Lumefantrine (20/120mg)", "2x2 for 3 days"
            elif (1 < age < 12) and (25 < weight < 34):
                return "Artenether/Lumefantrine (20/120mg)", "3x2 for 3 days"
            else:
                return "Artenether/Lumefantrine (20/120mg)", "4x2 for 3 days"


def prescript_symp(symptom: str) -> (str, [str, str] or str):
    if symptom.lower() == "breathlessness":
        return "ok", ["salbutamol inhaler", "1-2 puffs every 4hrs"]
    elif symptom.lower() == "high fever" or "headache":
        return "ok", ["Paracetamol", "2x3 for 3 days"]
    else:
        return "err", "_"


drug, presc1 = prescript_d(disease="malaria", age=10)

print(f"drug: {drug} \n prescription: {presc1}")

_, [drug, presc1] = prescript_symp("breathlessness")
print(f"drug: {drug} \n prescription: {presc1}")
