from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Age Classification API",
    description="Classifies a person's age group",
    version="1.0"
)

class UserInput(BaseModel):
    age: int = Field(gt=0, lt=120)

class PredictionResponse(BaseModel):
    age: int
    category: str

@app.get('/')
def home():
    return {"message": "Welcome Age Classification API"}

@app.post('/predict', response_model=PredictionResponse)
def predict(data: UserInput):

    age = data.age

    if age <= 12:
        category = "Child"

    elif age <= 19:
        category = "Teenager"

    elif age <= 59:
        category = "Adult"

    else:
        category = "Senior Citizen"

    return {
        "age": age,
        "category": category
    }