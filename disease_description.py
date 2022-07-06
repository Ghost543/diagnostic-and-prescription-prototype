import pandas as pd
import numpy as np

s_description = pd.read_csv("symptom_Description.csv")


def describe(disease: str) -> str:
    dic = s_description.to_dict()
    diseases = dic["Disease"]
    description = dic["Description"]

    diseases = list(diseases.values())
    description = list(description.values())
    dict_: dict = dict()
    for a, b in zip(diseases, description):
        dict_[a] = b
    return dict_[disease.capitalize()]


