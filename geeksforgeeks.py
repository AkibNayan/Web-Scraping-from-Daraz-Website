import requests
from bs4 import BeautifulSoup as bs
import pandas
page_no = 10
data = []
counter = 1
for page in range(1, page_no+1):
  re = requests.get(f"https://utilapi.geeksforgeeks.org/api/articles/?page={page}&gblog=true")
  response = re.json()
  length = len(response)
  for i in range(0, length):
    try:
      art_title = response[i]["article_title"]
    except:
      art_title = "Not Available"
    dict ={
        "serial" : counter,
        "title" : art_title
    }
    print(dict)
    data.append(dict)
    counter += 1
print(data)
df = pandas.DataFrame(data)
df.to_csv("GeeksforGeeks Article Title", index=False)
