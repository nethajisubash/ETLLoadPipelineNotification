import json
import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    glue_job_name = 'AutoETL.job'  # Replace with your actual Glue job name

    try:
        response = glue.start_job_run(JobName=glue_job_name)
        print(f"Subash-Started Glue job: {glue_job_name}, RunId: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': json.dumps(f"Subash-Started Glue job {glue_job_name} successfully!")
        }
    except Exception as e:
        print(f"Subash-Error starting Glue job: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps("Failed to start Glue job")
        }
