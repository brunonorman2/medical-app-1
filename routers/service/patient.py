from fastapi import HTTPException
from schema.patient import patients, Patients, PatientsCreateEdit

class PatientSerivce:

  @staticmethod
  def parse_patient(patient_data):
        data = []
        for cust in patient_data:
            data.append(patients[cust])
        return data

@staticmethod
def get_patient_by_id(patient_id):
        customer = patients.get(patient_id)
        if not customer:
            raise HTTPException(detail='patient not found.', status_code=404)
        return patients

@staticmethod
def create_patient(patient_data: PatientsCreateEdit):
        id = len(patients)
        patient = Patients(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient   
        return patient                                                                                                                 

@staticmethod
def edit_patient(payload: PatientsCreateEdit):
        id = len(patients)
        customer = Patients(
            id=id,
            **payload.model_dump()
        )
        patients[id] = patients
        return patients
    
@staticmethod
def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        del patient[patient_id]



