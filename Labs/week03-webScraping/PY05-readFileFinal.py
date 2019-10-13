# Lab 03 - Web Scraping
# Import the packages
from bs4 import BeautifulSoup # for displaying HTML
import csv # for reading / writing to csv

# Find and open the HTML file
with open("../week02/carviewer_Lab02.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Create the csv file and specify how it is written to
car_file = open("week02data.csv", mode="w")
car_writer = csv.writer(car_file, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)


# Read webpage and get a list of each row 
rows = soup.findAll("tr")

# Loop through each row
for row in rows:
    # Create a space to put the data in
    dataList = []
    # Find each column in each row
    cols = row.findAll("td")
    # Loop through each column in the row
    for col in cols:
       if not col.button: # Exclude the button elements
            # Append to the list, to just get the list of all the data
            dataList.append(col.text)
    # Write it to csv file 
    car_writer.writerow(dataList)

# Close the csv file
car_file.close()