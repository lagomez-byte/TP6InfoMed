import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        if resource_type == 'Patient':
            print(response.json()['id'])
            print(response.json()['identifier'][0]['value'])
            return response.json()['id'], response.json()['identifier'][0]['value'] 
        else:
            print(response.json()['id'])
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    if resource_type == "Patient":
        url = f"https://hapi.fhir.org/baseR4/{resource_type}?_pretty=true&identifier={resource_id}"
    else:
        url = f"http://hapi.fhir.org/baseR4/{resource_type}?subject={resource_id}&_pretty=true"
    #url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"}) 

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

