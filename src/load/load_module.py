from google.cloud import bigquery
#TODO Add exception handling
#TODO Add logging

def load_to_bq(fhir_resource_list,table_id):
    client = bigquery.Client()                                  # Construct a BigQuery client object.
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )
    load_job = client.load_table_from_json(                     # Make an API request.
        json_rows = fhir_resource_list,
        destination = table_id,
        location= "US",
        project = "cosmic-gizmo-269713",
        job_config=job_config,
    )                                                   
    assert load_job.job_type == "load"
    load_job.result()                                           # Waits for the job to complete.
    assert load_job.state == "DONE"
    table = client.get_table(table_id)
