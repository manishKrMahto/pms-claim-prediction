from pydantic import BaseModel , Field
from typing import Annotated, Optional, Literal

class PatientUpdate(BaseModel):
    
    name : Annotated[Optional[str] , Field(default=None, max_length=50, description= "name of the patient with limit of 50 character" )]
    city : Annotated[Optional[str] , Field(default=None, description="city of the patient")]
    age : Annotated[Optional[int] , Field(default=None, gt = 0 , description="age of the patient that cannot be negative")]
    gender : Annotated[Optional[Literal['Male','Female', 'Others']], Field(default=None,description="Gender of the Patient in between Male , Female or Others")]
    height : Annotated[Optional[float] , Field(default=None, description='Hieght of the patient in meters')]
    weight : Annotated[Optional[float], Field(default=None,description = 'Weight of the patient in KGs')]