# program to download data from bucket
from google.cloud import storage

storage_client = storage.Client.from_service_account_json('sunny-studio-246911-53844a4e564b.json')
bucket = storage_client.get_bucket('gcp-buck-1')
blob = bucket.get_blob('leny.jpg')  # file name in which you wanna save it on the GCP

# save to file
blob.download_to_filename('downloaded.jpg')

# save to file object
file_obj = open('using_obj.jpg', 'wb')
blob.download_to_file(file_obj)

print('Downloaded')