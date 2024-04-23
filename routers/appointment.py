from fastapi import APIRouter

from routers.service.appointment import AppointmentService
from schema.appointment import Appointments
from schema.patient import PatientsCreate, patients
from services.patient import PatientService

from schema.doctor import DoctorsCreate, Doctors
from services.doctor import DoctorService

patient_router = APIRouter()

doctor_router = APIRouter()

@appiontment_router.post('', status_code=201)
def create_appointment(payload: AppiontmentCreate): # type: ignore
  data = AppointmentService.create_appointment(payload)
  return {'message': 'success', 'data': data}

@Appointments.get('', status_code=200)
def get_appointment():
    return {'message': 'success', 'data': Appointments}

@appointment_router.get('/{appointment_id}')
def get_appointment_by_id(appointment_id: int):
    data = AppointmentService.get_appointment_by_id(appointment_id)
    return {'message': 'success',  'data': data}

@appointment_router.put('/{appointment_id}')
def update_appointment(appointment_id: int, payload: AppiontmentsCreate):
    data = AppointmentService.edit_appointment(appointment_id, payload)
    return {'message': 'success', 'data': data}

appointment_router.delete('/{appointment_id}', status_code=200)
def delete_appointment(doctor_id: int):
    AppointmentService.delete_appointment(appointment_id)
    return {'Flight deleted successfully.'}







