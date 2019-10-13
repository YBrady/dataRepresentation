# Lab 03 - Web Scraping
# Import the packages
from bs4 import BeautifulSoup # for displaying HTML

# Find and open the file
with open("../week02/carviewer_Lab02.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Print out the prettified page
print (soup.prettify())