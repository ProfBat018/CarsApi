from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year


cars = [
        Car("Mercedes", "CLS 63 AMG", 2014),
        Car("BMW", "M6", 2014),
        Car("AUDI", "RS 7", 2018),
        Car("Porsche", "911 Rough Welt", 1973)
]


@app.get("/{cars}")
async def all_cars():
    return {"message": cars}


@app.post("/add")
async def add(make: str = Form(...), model: str = Form(...), year: int = Form(...)):
    cars.append(Car(make, model, year))
