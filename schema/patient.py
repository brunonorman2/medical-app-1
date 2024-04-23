from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight:int
    height: float
    phone: str

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='patient 0', age=30,sex='male',weight=123,height=6, phone='0800'
    ),
    1: Patients(
        id=1, name='patient 1', age=35,sex='female',weight=150,height=5.4,phone='0801'
    ),
    2: Patients(
        id=2, name='patient 2', age=20,sex='female',weight=120,height=4.3, phone='0802'
    )
}

