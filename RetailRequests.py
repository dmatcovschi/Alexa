import csv
import requests
import re
from bs4 import BeautifulSoup

r = requests.get("http://www.alexa.com/topsites/category;0/Top/Shopping")
soup = BeautifulSoup(r.content)
subCollections = soup.find("ul", {"class" : "subcategories span3"})
print(subCollections)