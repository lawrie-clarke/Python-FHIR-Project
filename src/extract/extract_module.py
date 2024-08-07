import json
from fhir.resources.bundle import Bundle
from fhir.resources.R4B import construct_fhir_element
import requests
import io
import zipfile
#import fhir.resources

#TODO create function for repetitive json handling
#TODO seperate to three functions, 1 for import from web, 1 for import from local file, 1 for processing to seperate resources

#import from local file function
def import_from_local_file(file_path):
    #resources = []  
    patients = []    
    organizations = []
    practitioners = []
    encounters = []
    conditions = []
    medicationrequests = []
    claims = []
    careteams = []
    goals = []
    careplans = []
    explanationofbenefits = []
    observations = []
    procedures = []
    immunizations = []
    diagnostictreports = []                                             #initiate empty resource list
    with open(file_path) as json_file:
        data = json_file.read()                                         #convert to bytes
        bundle = construct_fhir_element('Bundle', data)                 #construct FHIR bundle so it's easier to work with
    if bundle.entry is not None:                       
        for entry in bundle.entry:
            #resources.append(entry.resource.json())
            if entry.resource.resource_type == 'Patient':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                patients.append(json_object)                            #add to list to make list of dictionaries (what bq expects)          
            elif entry.resource.resource_type == 'Organization':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                organizations.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Practitioner':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                practitioners.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Encounter':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                encounters.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Condition':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                conditions.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'MedicationRequest':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                medicationrequests.append(json_object)                  #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Claim':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                claims.append(json_object)                              #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'CareTeam':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                careteams.append(json_object)                           #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Goal':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                goals.append(json_object)                               #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'CarePlan':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                careplans.append(json_object)                           #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'ExplanationOfBenefit':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                explanationofbenefits.append(json_object)               #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Observation':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                observations.append(json_object)                        #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Procedure':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                procedures.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'Immunization':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                immunizations.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
            elif entry.resource.resource_type == 'DiagnosticReport':
                json_string = entry.resource.json()                     #convert to json string
                json_object = json.loads(json_string)                   #convert to json object
                diagnostictreports.append(json_object)                  #add to list to make list of dictionaries (what bq expects)
            else:
                continue
    #print(patients)
    return patients, organizations, practitioners, encounters, conditions, medicationrequests, claims, careteams, goals, careplans, explanationofbenefits, observations, procedures, immunizations, diagnostictreports
#import_from_local_file('/home/lawrieclarke/Python-FHIR-Project/Python-FHIR-Project/sample_full.json')

def import_from_web(url):
    response = requests.get(url)                                        #gets a html response which includes status, headers, body (not for get) and text
    #resources = []  
    patients = []    
    organizations = []
    practitioners = []
    encounters = []
    conditions = []
    medicationrequests = []
    claims = []
    careteams = []
    goals = []
    careplans = []
    explanationofbenefits = []
    observations = []
    procedures = []
    immunizations = []
    diagnostictreports = []  
    #TODO look at vectorising the nested for loop to improve performance
    with zipfile.ZipFile(io.BytesIO(response.content),"r") as zip:                  #convert to a file like object which zipfile can recognise and then make a zipfile object
        for member in zip.infolist():                                               #iterate over contents of zip file
            if not member.is_dir():                                                 #ignore the directories and just iterate over files
                with zip.open(member) as json_file:                                 #open the json files
                    data = json_file.read()                                         #convert to bytes 
                    try:
                        bundle = construct_fhir_element('Bundle', data)             #construct bundle
                    except ValueError:
                        print(json_file.name + " failed because of a ValueError")   #flag value error if issue with the contents
                if bundle.entry is not None:                       
                    for entry in bundle.entry:
                        #resources.append(entry.resource.json())
                        if entry.resource.resource_type == 'Patient':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            patients.append(json_object)                            #add to list to make list of dictionaries (what bq expects)          
                        elif entry.resource.resource_type == 'Organization':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            organizations.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Practitioner':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            practitioners.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Encounter':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            encounters.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Condition':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            conditions.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'MedicationRequest':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            medicationrequests.append(json_object)                  #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Claim':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            claims.append(json_object)                              #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'CareTeam':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            careteams.append(json_object)                           #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Goal':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            goals.append(json_object)                               #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'CarePlan':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            careplans.append(json_object)                           #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'ExplanationOfBenefit':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            explanationofbenefits.append(json_object)               #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Observation':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            observations.append(json_object)                        #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Procedure':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            procedures.append(json_object)                          #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'Immunization':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            immunizations.append(json_object)                       #add to list to make list of dictionaries (what bq expects)
                        elif entry.resource.resource_type == 'DiagnosticReport':
                            json_string = entry.resource.json()                     #convert to json string
                            json_object = json.loads(json_string)                   #convert to json object
                            diagnostictreports.append(json_object)                  #add to list to make list of dictionaries (what bq expects)
                        else:
                            continue
    #print(patients)
    return patients, organizations, practitioners, encounters, conditions, medicationrequests, claims, careteams, goals, careplans, explanationofbenefits, observations, procedures, immunizations, diagnostictreports  
#import_from_web("https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_fhir_r4_sep2019.zip")
