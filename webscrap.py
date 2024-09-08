import requests
from bs4 import BeautifulSoup 
import csv

#accessing html content
URL = "http://www.geeksforgeeks.org/DSA"
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')
print(soup.prettify())
print(soup.get_text())
