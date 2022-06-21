# export GOOGLE_APPLICATION_CREDENTIALS=/Users/piotr/Projects/key.json
# . venv/bin/activate   
from google.cloud import storage

bucket_name = "testborsuk"

# client = storage.Client()
# bucket = client.get_bucket(bucket_name)

def list_buckets():
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    return [bucket.name for bucket in buckets]

def list_blobs(bucket_name):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    return [blob.name for blob in blobs]


# buckets = list_buckets()
# print([list_blobs(bucket) for bucket in buckets])

