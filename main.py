import downloader
import grocery_links
import scraper

url = grocery_links.GROCERY_LINKS[0]

flyer_link = scraper.get_flyer_link(url)
print("Flyer link: " + flyer_link)

image_links = scraper.get_image_links(flyer_link)
print("Image links:")
print(image_links)

for idx, link in enumerate(image_links, start=1):
  downloader.download_image(link, "./images/basics-" + str(idx) + ".jpg")
