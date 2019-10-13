import csv # Read from  / Write to csv files

# Create a file (if not already existing and open in edit mode)
employee_file = open("employee_file.csv", mode = "w")
# Define in what format the data will be represented for entry into the file
employee_writer = csv.writer(employee_file,delimiter = ",", quotechar= '"', quoting= csv.QUOTE_MINIMAL)

# Start writing to the file with the data
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# Close the file after
employee_file.close()
