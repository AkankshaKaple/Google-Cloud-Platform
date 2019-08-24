# Program to upload data onto the bucket

from google.cloud import storage
storage_client = storage.Client.from_service_account_json('sunny-studio-246911-53844a4e564b.json')
bucket = storage_client.get_bucket('gcp-buck-1')
blob = bucket.blob('leny.jpg')
blob.upload_from_filename('the-big-bang-theory-e1558467645699.jpg')
print('Uploaded')
