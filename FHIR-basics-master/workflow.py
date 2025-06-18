from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir
from datetime import datetime
from condition import create_condition_resource

if __name__ == "__main__":
    family_name = "Denken"
    given_name = "Frieren"
    birth_date = "2002-06-22"
    gender = "female"
    phone = 5492494373221
    dni = 40909213


# Crear y enviar el recurso de paciente
patient = create_patient_resource(family_name, given_name, birth_date, gender, phone,dni)
patient_id,patient_dni = send_resource_to_hapi_fhir(patient, 'Patient')
subject_reference = f"Patient/{patient_id}"
diabetes_condition = create_condition_resource(
    subject_reference= subject_reference,
    condition_code="44054006",
    condition_display="Diabetes mellitus type 2",
    clinical_status="active",
    verification_status="confirmed",
    severity_code="6736007",
    severity_display="Moderate",
    body_site_code="122456002",
    body_site_display="Pancreas",
    onset_date= datetime(2020, 5, 15),
    note_text="Patient requires insulin management",
    text_div="<div xmlns='http://www.w3.org/1999/xhtml'>Diabetes mellitus type 2 (Moderate)</div>"
)

if patient_id:
    send_resource_to_hapi_fhir(diabetes_condition, "Condition")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    get_resource_from_hapi_fhir(patient_dni,'Patient')
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    get_resource_from_hapi_fhir(patient_id,'Condition')
