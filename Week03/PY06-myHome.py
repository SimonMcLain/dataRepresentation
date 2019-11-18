cdimport requests
import csv
from bs4 import  BeautifulSoup
url = "https://myhome.ie/residential/mayo/property-for-sale?page-1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard__Address")

for listing in listings:
  entryList = []

  price = listings.find(class_="PropertyListingCard__Price").text
  entryList.append(price)
  address = listing.find(class_="PropertyListingaCard__Address").text
  entryList.append(address)

  home_writer.writerow(entryList)
home_file.close()