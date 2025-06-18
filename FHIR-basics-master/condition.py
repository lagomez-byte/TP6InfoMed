from datetime import datetime
from fhir.resources.condition import Condition
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.narrative import Narrative
from fhir.resources.annotation import Annotation

def create_condition_resource(
    subject_reference: str, 
    condition_code: str,     
    condition_display: str,  
    clinical_status: str = "active",
    verification_status: str = "confirmed",
    severity_code: str = None,
    severity_display: str = None,
    body_site_code: str = None,
    body_site_display: str = None,
    onset_date: datetime = None,
    abatement_date: datetime = None,
    recorded_date: datetime = None,
    note_text: str = None,
    encounter_reference: str = None,
    text_div: str = None
) -> Condition:
    
    condition = Condition(
        subject=Reference(reference=subject_reference),
        code=CodeableConcept(
            coding=[Coding(
                system="http://snomed.info/sct",
                code=condition_code,
                display=condition_display
            )],
            text=condition_display
        ),
        clinicalStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/condition-clinical",
                code=clinical_status
            )]
        ),
        verificationStatus=CodeableConcept(
            coding=[Coding(
                system="http://terminology.hl7.org/CodeSystem/condition-ver-status",
                code=verification_status
            )]
        )
    )

    if severity_code and severity_display:
        condition.severity = CodeableConcept(
            coding=[Coding(
                system="http://snomed.info/sct",
                code=severity_code,
                display=severity_display
            )]
        )

    if body_site_code and body_site_display:
        condition.bodySite = [CodeableConcept(
            coding=[Coding(
                system="http://snomed.info/sct",
                code=body_site_code,
                display=body_site_display
            )]
        )]

    if onset_date:
        condition.onsetDateTime = onset_date.isoformat()

    if abatement_date:
        condition.abatementDateTime = abatement_date.isoformat()

    if recorded_date:
        condition.recordedDate = recorded_date.isoformat()

    if note_text:
        condition.note = [Annotation(text=note_text)]

    if encounter_reference:
        condition.encounter = Reference(reference=encounter_reference)

    if text_div:
        condition.text = Narrative(
            status="generated",
            div=text_div
        )

    return condition
