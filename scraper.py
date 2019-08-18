from bs4 import BeautifulSoup
import urllib2
import re

# url = "https://flyers.smartcanucks.ca/walmart-canada"
# header = {'User-Agent': 'Mozilla/5.0'}
# req = urllib2.Request(url, headers=header)
# content = urllib2.urlopen(req)
# soup = BeautifulSoup(content)

# current_flyer_links = []
# pattern = "\-on\-|\-gta\-"

# for link in soup.find_all('a'):
#   href = link.get('href')
#   if re.search(pattern, href):
#     current_flyer_links.append(href + "/all")
#     break

# print(current_flyer_links)

def get_flyer_link(url):
  soup = getContent(url)
  pattern = "\-on\-|\-gta\-"
  target_link = ""

  for link in soup.find_all('a'):
    href = link.get('href')
    if re.search(pattern, href):
      target_link = href + "/all"
      break

  return target_link

def getContent(url):
  header = {'User-Agent': 'Mozilla/5.0'}
  req = urllib2.Request(url, headers=header)
  content = BeautifulSoup(urllib2.urlopen(req))
  return content
  
def get_image_links(url):
  image_links = []
  soup = getContent(url)
  pattern = "\/uploads\/pages\/"

  for img in soup.find_all('img'):
    src = img.get('src')
    if re.search(pattern, src):
      image_links.append(src)
  
  return image_links