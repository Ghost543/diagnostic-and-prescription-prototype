import numpy as np
import pandas as pd
import os

data_1 = pd.read_csv("dataset.csv")
data_2 = pd.read_csv("Symptom-severity.csv")
selected_diseases = ["Malaria", "Typhoid", "Tuberculosis", "Common Cold", "Pneumonia"]
data_1 = data_1[data_1.Disease.isin(selected_diseases)]

data_1 = pd.DataFrame(data_1).reset_index(drop=True)

data_2['Symptom'] = data_2['Symptom'].str.replace('_', ' ')

ss = data_2.to_dict()
symp, weig = ss.keys()
sy = ss[symp]
we = ss[weig]
sevirity_dict = {}
for i in range(len(sy)):
    sevirity_dict[sy[i]] = we[i]

symptoms = list(data_2["Symptom"].str.strip().values)
symptoms_dict = {}
for i in range(len(symptoms)):
    symptoms_dict[symptoms[i]] = i + 1

Y = data_1["Disease"].values


def converter(arr: list):
    length_arr = len(arr)
    sm = 0
    for i in arr:
        v = sevirity_dict[i.strip().lower()]
        sm += v
    deff = 18 - length_arr
    for i in range(length_arr):
        arr[i] = symptoms_dict[arr[i].strip().replace("_", " ").lower()]

    if length_arr != 17:
        for i in range(deff - 1):
            arr.append(0)
        arr.append(sm)
    return np.array([arr]).astype("float32")
