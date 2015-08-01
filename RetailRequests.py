import csv
import requests
import re
from bs4 import BeautifulSoup

url = "http://www.alexa.com/topsites/category;0/Top/Shopping"
coreURL = "http://www.alexa.com"

urlCategories = []

def findCategories(baseURL):
	r = requests.get(baseURL)
	soup = BeautifulSoup(r.content)
	subCollections = soup.find_all("ul", {"class" : "subcategories span3"})

	for subCollection in subCollections:
		for sub in subCollection:
			linkSub = coreURL + sub.find("a",href=True)["href"]
			print(linkSub)
			
			urlCategories.append(linkSub)

			if BeautifulSoup(requests.get(linkSub).content).find("ul", {"class" : "subcategories span3"}) == None:
				continue	
			else:
				findCategories(linkSub)

def Category(categoryURL):
	r = requests.get(categoryURL)
	soup = BeautifulSoup(r.content)
	siteCollection = soup.find_all("li", {"class" : "site-listing"})	
	linkSite = site.find("a",href=True)["href"]
	siteName = site.find("a").text
	print(siteName)

	


#coreURL = "www.alexa.com"


#get all categories
#for sub in subCollections:
#	linkSub = sub.find("a",href=True)
	#print(coreURL + linkSub["href"])

#siteCollection = soup.find_all("li", {"class" : "site-listing"})
#for site in siteCollection:
#	linkSite = site.find("a",href=True)["href"]
#	siteName = site.find("a").text	
	#print(siteName)

#siteRequest = requests.get("http://www.alexa.com/siteinfo/amazon.com")
#soupSite = BeautifulSoup(siteRequest.content)


#globalRank = soupSite.find("strong", {"class" : "metrics-data align-vmiddle"}).text
#bounceRate = soupSite.find("span", {"data-cat" : "bounce_percent"}).strong.text

#print(soupSite)

findCategories(url)