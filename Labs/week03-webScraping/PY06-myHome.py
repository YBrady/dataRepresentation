# Lab 03 - Web Scraping
# Import the packages
import requests # for HTTP
from bs4 import BeautifulSoup # for displaying HTML
import csv # for reading / writing to csv

# Set the page to work on
page = requests.get("https://www.myhome.ie/residential/cork/property-for-sale-in-cork-city")

# Create the soup
soup = BeautifulSoup(page.content, "html.parser")

# Create the csv file and specify how it is written to. 
# Note newline parameter - ensures there is not a spare line between entries
home_file = open("week03MyHome.csv", mode="w", newline='')
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Collect all the listings
listings = soup.findAll("div", class_="PropertyListingCard" ) 

# Loop through each of the listings
for listing in listings: 
    # Create the empty list for row population
    entryList = [] 
    # Find the price for each listing
    price = listing.find(class_="PropertyListingCard__Price").text 
    # Add it to the list
    entryList.append(price) 
    # Find the address for each listing
    address = listing.find(class_="PropertyListingCard__Address").text 
    # Add it to the list
    entryList.append(address) 
    # Write the list contents to a new row in the csv
    home_writer.writerow(entryList)
# Close the file when you are done
home_file.close()