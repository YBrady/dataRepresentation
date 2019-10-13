# Lab 03 - Web Scraping

# First off import the required packages
import requests # HTTP library for Python, safe for human consumption.
from bs4 import BeautifulSoup # Makes the pulled back html data easier to read

# Specify the site you want to the info from
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# Print the return value - 200 = success
print(page)
print("---------------")
# Print the page content
print(page.content)
soup1 = BeautifulSoup(page.content,"html.parser")
print("---------------")
print(soup1.prettify()