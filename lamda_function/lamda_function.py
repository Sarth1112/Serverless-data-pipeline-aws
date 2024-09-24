import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')
    
    processed_data = file_content.upper()  # Example transformation
    
    processed_key = file_key.replace('raw/', 'processed/')
    s3.put_object(Body=processed_data, Bucket=bucket_name, Key=processed_key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed and saved in ' + processed_key)
    }
