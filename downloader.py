import requests

def download_image(url, filename):
  img_data = requests.get(url).content
  with open(filename, 'w+') as handler:
    handler.write(img_data)