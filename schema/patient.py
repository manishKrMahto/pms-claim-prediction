from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

# --------------------- Utilities for Patient Management --------------------- #

def load_data():
    with open("models/patients.json", "r") as f:
        data = json.load(f)
    return data

def dump_data(data):
    with open("models/patients.json", 'w') as f:
        json.dump(data, f)

# --------------------- Pydantic Models --------------------- #

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Patient ID", examples=["P001"])]
    name: Annotated[str, Field(..., max_length=50, description="Name of the Patient")]
    city: Annotated[str, Field(..., description="City")]
    age: Annotated[int, Field(..., gt=0, description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(...)]
    height: Annotated[float, Field(..., description="Height in meters")]
    weight: Annotated[float, Field(..., description="Weight in kg")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        return "Obese"

class PatientUpdate(BaseModel):
    name: Optional[str]
    city: Optional[str]
    age: Optional[int]
    gender: Optional[Literal["Male", "Female", "Others"]]
    height: Optional[float]
    weight: Optional[float]