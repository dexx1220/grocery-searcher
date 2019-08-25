import config
import downloader
import groceries
import image_analyzer
import scraper
import time
import uploader

groceries_data = groceries.GROCERY_DATA
desired_items = groceries.GROCERY_ITEMS
grocery_search_results = {}

for i, item in enumerate(groceries_data, start=1):
  store_name = item.get('name')
  url = item.get('link')
  grocery_search_results[store_name] = {'pages': []}

  flyer_link = scraper.get_flyer_link(url, item.get('excludeProvince'))
  image_links = scraper.get_image_links(flyer_link)

  for idx, link in enumerate(image_links, start=1):
    image_name = store_name + "-" + str(idx) + ".jpg"
    downloader.download_image(link, "./images/" + image_name)
    source = uploader.upload_image(config.BUCKET_NAME, image_name, "./images/" + image_name)
    detection_results = image_analyzer.detect_text(source, desired_items)
    if (len(detection_results) > 0):
      pages = grocery_search_results[store_name].get('pages')
      pages.append(link)

  if (i < len(groceries_data)):
    print("=== SLEEPING FOR 10 SECONDS ===")
    time.sleep(10)
