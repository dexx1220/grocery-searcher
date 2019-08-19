import downloader
import groceries
import scraper
import time

groceries_data = groceries.GROCERY_DATA

for i, item in enumerate(groceries_data, start=1):
  store_name = item.get('name')
  url = item.get('link')

  flyer_link = scraper.get_flyer_link(url)
  image_links = scraper.get_image_links(flyer_link)

  for idx, link in enumerate(image_links, start=1):
    downloader.download_image(link, "./images/" + store_name + "-" + str(idx) + ".jpg")
  
  if (i < len(groceries_data)):
    print("=== SLEEPING FOR 10 SECONDS ===")
    time.sleep(10)
