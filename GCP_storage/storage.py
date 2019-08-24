# Program to create bucket in GCP
from google.cloud import storage
bucket_name = 'gcp-buck-1'
storage_client = storage.Client.from_service_account_json(
    'sunny-studio-246911-53844a4e564b.json')
bucket = storage_client.create_bucket(bucket_name)
print('Bucket {} created'.format(bucket.name))
