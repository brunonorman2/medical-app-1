from pydantic import BaseModel

class Doctors(BaseModel):
    from schema.patient import patients,Patients
    id: int
    name:str
    specialization: str
    phone: int
    

doctor: list[Doctors] = [
    Doctors(
        id=0,name='Doctor 0', specialization='eye',
        phone='0808'
    ),
    Doctors(
        id=0,name='Doctor 1', specialization='teeth',
        phone='0807'
    ),
]