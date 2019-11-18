from bs4 import BeautifulSoup

with open("../Week 2/carviewerv2.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')
print(soup.prettify())