from google.cloud import vision
client = vision.ImageAnnotatorClient()

def detect_text(source, target_words):
  print("=== DETECTING TEXT FOR: " + source + " ===")
  image = vision.types.Image()
  image.source.image_uri = source
  response = client.text_detection(image=image)
  text_annotations = response.text_annotations
  print("=== TEXT ANNOTATIONS ===")
  print(text_annotations)
  results = filter(lambda obj: obj.description.lower() in target_words, text_annotations)
  print("=== RESULTS ===")
  print(results)
  return results