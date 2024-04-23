from fastapi import HTTPException

from schema.appointment import Appointments, Appointmentscreate
from schema.doctor import DoctorsCreate, Doctors, doctors
from schema.patient import Patients, patients

class AppointmentService:

    @staticmethod
    def create_appointment(payload: Appointmentscreate):
        id = len(Appointments)
        patient: Patients = patient[payload.patient]

id=id,
name=str
specialization= str
phone= str

@staticmethod
def get_appointment_by_id(appointment_id: int):
 if not Appointments:
            raise HTTPException(detail='Appointment not found', status_code=404)
            return AppointmentService
    
@staticmethod
def update_appointment(appointment_id: int, payload: Appointmentscreate):
        appointment: AppointmentService  =appointment.get (appointment_id)
        if not appointment:
            raise HTTPException(detail='Flight not found', status_code=404)
        appointment: Appointments = appointment[payload.appointment]
    
@staticmethod
def delete_appointmant(appointment_id):
        
        if not doctors:
            raise HTTPException(detail='Doctor not found', status_code=404)
        del doctors[doctors]