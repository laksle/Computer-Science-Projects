#this program scrapes good reads data via a direct book url

import re
import time
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
##copy chromedriver into python folder
driver = webdriver.Chrome()
driver.set_window_position(-2000,0)#this function will minimize the window
driver.get("https://www.goodreads.com/book/show/9917879-the-unwanteds?ref=rae_1")  # <------enter desired url here
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'lxml')
title = soup.find("h1").text
author = soup.find("h3", {"class": "Text Text__title3 Text__regular"}).text
data = ""
pages = ''
date = ''
published = soup.find(class_="FeaturedDetails")
rating = float(soup.find(class_="RatingStatistics__rating").text)
ratingStats = soup.find(class_='RatingStatistics__meta', attrs={"aria-label"}).text
ratingStats = ratingStats.replace("ratings", "ratings ")
genre = str(soup.findAll(class_="BookPageMetadataSection__genreButton"))
genre = re.sub(r'<.*?>', '', genre)
series = soup.find("h3", {"class": "Text Text__title3 Text__italic Text__regular Text__subdued"})

i = 0
for data in published:
    if pages == "":
        pages = data.get_text()
    if i == 1:
        date = data.get_text()
    i = 1
print("Title:", title)
try:
    print("Series:", series.text)
except:
    print("Series: None")
print('Author:', author)
print("Description:",pages)
print(date, end="\n")
print('Average Rating:', rating, 'stars')
print("Total:",ratingStats)
print("Genres:", genre)
