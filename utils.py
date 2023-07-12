import numpy as np
import json
import pickle
import os
import CONFIG


class HeartPrediction:

    def load_raw(self):
        with open(CONFIG.MODEL_FILE_PATH, "rb") as file:
            self.model = pickle.load(file)

        with open(CONFIG.JSON_FILE_PATH, "r") as json_file:
            self.columns = json.load(json_file)
        return "Success Load Raw Data"

    def __init__(self):
        print(os.getcwd())

    def predict_result(self, data):
        self.load_raw()
        self.data = data

        user_input = np.zeros([1, self.model.n_features_in_])
        self.model.feature_names = self.columns

        age = self.data["age"]
        gender = self.data["gender"]
        cp = self.data["cp"]
        trestbps = self.data["trestbps"]
        chol = self.data["chol"]
        fbs = self.data["fbs"]
        restecg = self.data["restecg"]
        thalach = self.data["thalach"]
        exang = self.data["exang"]
        oldpeak = self.data["oldpeak"]
        slope = self.data["slope"]
        ca = self.data["ca"]
        thal = self.data["thal"]

        user_input[0, 0] = float(age)
        user_input[0, 1] = float(gender)
        user_input[0, 2] = float(cp)
        user_input[0, 3] = float(trestbps)
        user_input[0, 4] = float(chol)
        user_input[0, 5] = float(fbs)
        user_input[0, 6] = float(restecg)
        user_input[0, 7] = float(thalach)
        user_input[0, 8] = float(exang)
        user_input[0, 9] = float(oldpeak)
        user_input[0, 10] = float(slope)
        user_input[0, 11] = float(ca)
        user_input[0, 12] = float(thal)

        print(f"User input = {user_input}")

        pred = self.model.predict(user_input)[0]
        print(f"Predict = {pred}")

        if pred == 0:
            print("No, You Don't have Heart Disease")
            return "No, You Don't have Heart Disease"
        elif pred == 1:
            print("Yes, You have Heart Disease")
            return "Yes, You have Heart Disease"


if __name__ == "__main__":
    pred_obj = HeartPrediction()
    pred_obj.load_raw()
