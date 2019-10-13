# Lab 03 - Web Scraping
# Import the packages
from bs4 import BeautifulSoup # for displaying HTML

# Find and open the file
with open("../week02/carviewer_Lab02.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Read file and get a list of each row 
rows = soup.findAll("tr")

# Loop through each row
for row in rows:
    # Create a space to put the data in
    dataList = []
    # Find each column in each row
    cols = row.findAll("td")
    # Loop through each column in the row
    for col in cols:
        # Append to the list, to just get the list of all the data
        dataList.append(col.text)
    # Print it out
    print(dataList)