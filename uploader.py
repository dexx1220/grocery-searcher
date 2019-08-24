from google.cloud import storage
client = storage.Client()

def upload_image(bucket_name, destination_file_name, source_file_path):
  bucket = client.get_bucket(bucket_name)
  blob = bucket.blob(destination_file_name)
  blob.upload_from_filename(filename=source_file_path)
  blob.make_public()
  return blob.public_url