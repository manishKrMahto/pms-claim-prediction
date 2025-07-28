from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.patient import Patient, load_data, dump_data
from schema.update_patient import PatientUpdate
from models.predict import predict_claim_category, model , MODEL_VERSION

# --------------------- FastAPI App --------------------- #

app = FastAPI(title="Patient Management + Insurance Predictor API")

# --------------------- API Endpoints --------------------- #

@app.get("/")
def root():
    return {"message": "Welcome to the Patient Management + Insurance Prediction API"}

@app.get("/about")
def about():
    return {"message": "Handles patient CRUD and predicts insurance category using ML model"}

# Machine Readable endpoint
# this endpoint is REQUIRED , used by the docker/kubernetives/cloud to check api working or not
@app.get("/health")
def health():
    return {
        "status" : "OK", 
        "version" : MODEL_VERSION , 
        "model loaded" : 'successfully' if model is not None else "UNSUCCESSFully"
    }

# ------------------ Patient Management Endpoints ------------------ #

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    data[patient.id] = patient.model_dump(exclude=["id"])
    dump_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully!"})

@app.get("/view")
def view_all():
    return load_data()

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return data[patient_id]

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, update: PatientUpdate):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    current = data[patient_id]
    
    update_data = update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        current[key] = value
        
    current["id"] = patient_id
    current.pop("bmi", None)
    current.pop("verdict", None)
    
    updated = Patient(**current)
    
    data[patient_id] = updated.model_dump(exclude=["id"])
    dump_data(data)
    
    return {"message": "Patient updated successfully"}

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]
    dump_data(data)
    
    return {"message": "Patient deleted successfully"}

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort by: height, weight, or bmi"),
    order: str = Query("asc", description="asc or desc")
):
    if sort_by not in ["height", "weight", "bmi"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order value")
    
    data = load_data()
    reverse = order == "desc"
    sorted_patients = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=reverse)
    
    return sorted_patients

# ------------------ Insurance Prediction Endpoint ------------------ #

@app.post("/predict")
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        prediction = predict_claim_category(user_input)
        return JSONResponse(status_code=200, content={"predicted_category": prediction})
    
    except Exception as e:
        return HTTPException(status_code=500, detail={str(e)})