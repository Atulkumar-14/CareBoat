#a function that is defined here but used somewhere else it take list of str as input and then import model form file ML_Model model load using joblib and then predict the output and return it as a dictionary
import joblib
import numpy as np
from pathlib import Path
def predict(user_symptoms: list[str]):

    # data = joblib.load("../../ML_Model/Mymodel_2.pkl")
    

    BASE_DIR = Path(__file__).resolve().parent
    model_path = BASE_DIR.parent.parent / "ML_Model" / "Mymodel_2.pkl"

    
    data = joblib.load(model_path)

    model = data["model"]
    symptoms = data["symptoms"]
    le = data["label_encoder"]

        # create empty vector
    input_vector = np.zeros(len(symptoms))

    # mark symptoms as 1
    for symptom in user_symptoms:
        if symptom in symptoms:
            index = symptoms.index(symptom)
            input_vector[index] = 1

    input_vector = input_vector.reshape(1, -1)

    prediction = model.predict(input_vector)

    disease = le.inverse_transform(prediction)

    return disease[0]