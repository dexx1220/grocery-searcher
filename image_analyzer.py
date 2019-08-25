from google.cloud import vision

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://dexx1220-flyer-bucket/doge.jpg'

response = client.text_detection(image=image)

print("@@@")
print(response.text_annotations)