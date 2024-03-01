#Import Libraries
import requests as re
import pandas as pd
import json
total_page = 14
data = []
for page_no in range(1, total_page+1):
  url = f"https://www.daraz.com.bd/featurephones/?ajax=true&page={page_no}&spm=a2a0e.home.cate_6.2.26c612f7AN2o92"
  res = re.get(url)
  response = res.json()
  total_items = len(response["mods"]["listItems"])
  for i in range(total_items):
    try:
      originalPrice = response["mods"]["listItems"][i]["originalPrice"]
      price = response["mods"]["listItems"][i]["price"]
      discount = response["mods"]["listItems"][i]["discount"]
      rating = response["mods"]["listItems"][i]["ratingScore"]
      review = response["mods"]["listItems"][i]["review"]
    except:
      originalPrice = "Not Available"
      price = "Not Available"
      discount = "Not Available"
      rating = "Not Available"
      review = "Not Available"
    dict = {
        "title" : response["mods"]["listItems"][i]["name"],
        "product_url" : 'https:' + response["mods"]["listItems"][i]["productUrl"],
        "originalPrice" : originalPrice,
        "price" : price,
        "discount" : discount,
        "rating" : rating,
        "review" : review
    }
    data.append(dict)
  print(f"Data Scraping from daraz featured phone {page_no} no page is done")
df = pd.DataFrame(data)
df.to_csv("daraz featured phone", index=False)