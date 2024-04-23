from fastapi import FastAPI

from routers.patient import patient_router
from routers.doctor import doctor_router

app = FastAPI()


app.include_router(router=patient_router, prefix='/patient', tags=['patient'])
app.include_router(router=doctor_router, prefix='/doctor', tags=['doctor'])

@app.get('/home')
def index():
    return "welcome Customer"

