import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)

"""driver.get("https://www.daraz.com.bd/smartphones/?spm=a2a0e.home.cate_6.1.735212f7SWIYUE")"""

"""titles = driver.find_elements('xpath', '//div[@id="id-title"]')
for title in titles:
    print(title.text)"""

"""ratings = driver.find_elements('xpath', '//span[@class="ratig-num--KNake rating--pwPrV"]')
for rating in ratings:
    print(rating.text)"""

"""ratings_count = driver.find_elements('xpath', '//span[@class="rating__review--ygkUy rating--pwPrV"]')
for rating_count in ratings_count:
    print(rating_count.text)"""

"""unit_solds = driver.find_elements('xpath', '//div[contains(text(), "Sold")]')
for unit_sold in unit_solds:
    print(unit_sold.text)"""

"""prices = driver.find_elements('xpath', '//span[@class="currency--GVKjl"]')
for price in prices:
    print(price.text)"""


"""org_prices = driver.find_elements('xpath', '//del[@class="currency--GVKjl"]')
for org_price in org_prices:
    print(org_price.text)"""

data = []
for page in range(1, 14):
    driver.get(f'https://www.daraz.com.bd/smartphones/?page={page}&spm=a2a0e.searchlistcategory.pagination.2.2d32310cPwzPfj')

    # Not to detect as Bot use sleep()
    time.sleep(1)
    
    titles = driver.find_elements('xpath', '//div[@id="id-title"]')
    totalTitle = len(titles)

    for item in range(1, totalTitle+1):
        try:
            title = driver.find_element(
                'xpath', f'(//div[@id="id-title"])[{item}]').text
        except:
            title = "Not Available"
        try:
            rating = driver.find_element(
                'xpath', f'(//span[@class="ratig-num--KNake rating--pwPrV"])[{item}]').text
        except:
            rating = "Not Available"
        try:
            rating_count = driver.find_element(
                'xpath', f'(//span[@class="rating__review--ygkUy rating--pwPrV"])[{item}]').text
        except:
            rating_count = "Not Available"
        try:
            unit_sold = driver.find_element(
                'xpath', f'(//div[contains(text(), "Sold")])[{item}]').text
        except:
            unit_sold = "Not Available"
        try:
            price = driver.find_element(
                'xpath', f'(//span[@class="currency--GVKjl"])[{item}]').text
        except:
            price = "Not Available"
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            org_price = driver.find_element(
                'xpath', f'(//del[@class="currency--GVKjl"])[{item}]').text
        except:
            org_price = "Not Available"
        dict_ = {
            'title': title,
            'rating': rating,
            'rating_count': rating_count,
            'unit_sold': unit_sold,
            'price': price,
            'org_price': org_price
        }
        data.append(dict_)
    

"""df = pd.DataFrame(data)
df.to_csv("DarazSPhoneDataSeleniumCrack.csv", index=False)"""
print(data)
