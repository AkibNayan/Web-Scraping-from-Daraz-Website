#Web Extraction / Web Scraping / Web Crawling From Daraz "Smart Phone Sub Category"
import requests as re
import pandas as pd
import json
url = "https://www.daraz.com.bd/smartphones/?ajax=true&page=1&spm=a2a0e.home.cate_6.1.735212f7I5rFs6"
total_page = 12
data = []
for page_no in range(1, total_page+1):
  url = f"https://www.daraz.com.bd/smartphones/?ajax=true&page={page_no}&spm=a2a0e.home.cate_6.1.735212f7I5rFs6"
  res = re.get(url)
  response = res.json()
  total_items = len(response["mods"]["listItems"])
  for i in range(total_items):
    try:
      original_price = response["mods"]["listItems"][i]["originalPrice"]
      price = response["mods"]["listItems"][i]["price"]
      discount = response["mods"]["listItems"][i]["discount"]
      rating = response["mods"]["listItems"][i]["ratingScore"]
      review_count = response["mods"]["listItems"][i]["review"]
    except:
      original_price = "Not Available"
      price = "Not Available"
      discount = "Not Available"
      rating = "Not Available"
      review_count = "Not Available"
    dict = {
        "title" : response["mods"]["listItems"][i]["name"],
        "product_url" : 'https:' + response["mods"]["listItems"][i]["productUrl"],
        "original_price" : original_price,
        "price" : price,
        "discount" : discount,
        "rating" : rating,
        "review_count" : review_count
    }
    data.append(dict)
  print(f'Page number {page_no} is Done')
df = pd.DataFrame(data)
df.to_csv('Daraz Smart Phone Data', index = False)
