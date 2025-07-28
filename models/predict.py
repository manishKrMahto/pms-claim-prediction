import pickle
import pandas as pd

# --------------------- Model Version -------------------- #
MODEL_VERSION = '1.0.0'

# --------------------- Load ML Model --------------------- #
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_claim_category(user_input : dict):
    input_df = pd.DataFrame([user_input])
    
    output = model.predict(input_df)[0] 

    return output 
