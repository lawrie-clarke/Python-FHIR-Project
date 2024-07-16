import extract_module
import load_module
import os

#set environment defaults
os.environ.setdefault("GCLOUD_PROJECT", "cosmic-gizmo-269713")

#import synthea data from web and seperate to individual fhir resources lists for loading to BQ
patients, organizations, practitioners, encounters, conditions, medicationrequests, claims, careteams, goals, careplans, explanationofbenefits, observations, procedures, immunizations, diagnostictreports = extract_module.import_from_web("https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_fhir_r4_sep2019.zip",'fhir/Willian804_Moen819_439b24b4-6f25-4093-b101-47a39bd061ca.json')

#load fhir data to BQ
load_module.load_to_bq(patients,"cosmic-gizmo-269713.python_fhir_project.Patient")
load_module.load_to_bq(organizations,"cosmic-gizmo-269713.python_fhir_project.Organization")
load_module.load_to_bq(practitioners,"cosmic-gizmo-269713.python_fhir_project.Practitioner")
load_module.load_to_bq(encounters,"cosmic-gizmo-269713.python_fhir_project.Encounter")
load_module.load_to_bq(conditions,"cosmic-gizmo-269713.python_fhir_project.Condition")
load_module.load_to_bq(medicationrequests,"cosmic-gizmo-269713.python_fhir_project.MedicationRequest")
load_module.load_to_bq(claims,"cosmic-gizmo-269713.python_fhir_project.Claim")
load_module.load_to_bq(careteams,"cosmic-gizmo-269713.python_fhir_project.CareTeam")
load_module.load_to_bq(goals,"cosmic-gizmo-269713.python_fhir_project.Goal")
load_module.load_to_bq(careplans,"cosmic-gizmo-269713.python_fhir_project.CarePlan")
load_module.load_to_bq(explanationofbenefits,"cosmic-gizmo-269713.python_fhir_project.ExplanationOfBenefit")
load_module.load_to_bq(observations,"cosmic-gizmo-269713.python_fhir_project.Observation")
load_module.load_to_bq(procedures,"cosmic-gizmo-269713.python_fhir_project.Procedure")
load_module.load_to_bq(immunizations,"cosmic-gizmo-269713.python_fhir_project.Immunization")
load_module.load_to_bq(diagnostictreports,"cosmic-gizmo-269713.python_fhir_project.DiagnosticReport")

