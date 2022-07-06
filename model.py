from operator import mod
from textwrap import indent
import numpy as np
import pandas as pd
import tensorflow as tf
# from tensorflow.keras.utils import plot_model
import os

data_1 = pd.read_csv("dataset.csv")
data_2 = pd.read_csv("Symptom-severity.csv")
selected_diseases = ["Malaria", "Typhoid", "Tuberculosis", "Common Cold", "Pneumonia"]
data_1 = data_1[data_1.Disease.isin(selected_diseases)]

data_1 = pd.DataFrame(data_1).reset_index(drop=True)

data_2['Symptom'] = data_2['Symptom'].str.replace('_', ' ')

class Diagonistic:
    def  __init__ (self, symptoms: list):
        self.symptoms = symptoms


        ss = data_2.to_dict()
        symp, weig = ss.keys()
        sy = ss[symp]
        we = ss[weig]
        self.sevirity_dict = {}
        for i in range(len(sy)):
            self.sevirity_dict[sy[i]] = we[i]

        self.symptoms_ = list(data_2["Symptom"].str.strip().values)
        self.symptoms__dict = {}
        for i in range(len(self.symptoms_)):
            self.symptoms__dict[self.symptoms_[i]] = i + 1

        self.Y = data_1["Disease"].values
        self.Y = np.unique(self.Y)

        self.model = tf.keras.models.load_model("nn_model1.h5")


       

    def converter(self, arr) -> np.ndarray:
        length_arr = len(arr)
        sm = 0
        for i in arr:
            if type(i) == int:
                continue
            v = self.sevirity_dict[i.strip().lower()]
            sm += v
        deff = 13 - length_arr
        for i in range(length_arr):
            arr[i] = self.symptoms__dict[arr[i].strip().replace("_", " ").lower()]

        if length_arr != 12:
            for i in range(deff - 1):
                arr.append(0)
            arr.append(sm)
        return np.array([arr]).astype("float32")

    def predict(self):
        test = self.converter(self.symptoms)
        self.test_pt =self. model.predict(test)
        print(self.test_pt)

        return self.Y[np.argmax(self.test_pt)]
    def prob_val(self):
        return round(np.max(self.test_pt) * 100, 2)

    def sec_prediction(self):
        copy = self.test_pt
        copy_ = list(copy.flatten())
        copy__ = list(copy.flatten())
        copy_h = copy_.pop(np.argmax(copy))
        self.max_val = max(copy_)
        ind_max = copy__.index(self.max_val)
        self.sec_val_pt = self.Y[ind_max]
        return self.sec_val_pt
    
    def sec_prob_val(self):
        return round(self.max_val * 100, 2)







# print(Y[np.argmax(test_pt)])

# model.summary()

# plot_model(model, to_file='model.png', show_shapes=True)

# ff = Diagonistic(["chills","vomiting","high fever","headache","nausea","muscle pain"])
# ff_test = ff.predict()


# print(ff_test)