# Import required libraries
import csv
from splinter import Browser

# Define key variables
csv_filename = "sample_data.csv"  # The file should be relative to the directory containing this file
form_url = "https://goo.gl/forms/D8DLeJawU91srNCB2"

# Read the CSV file and process each row
with open(csv_filename, mode='r') as csv_file:  # Open the CSV file in read mode
    csv_reader = csv.DictReader(csv_file)  # Load CSV contents into a dictionary
    line_count = 0  # Start a count for the number of lines
    for row in csv_reader:  # Loop over each row in the CSV file. The first row (containing column names} is automatically skipped
        """
        Available variables (these correspond to the column names in the CSV file):
        row['Name']
        row['Email']
        row['Address']
        row['Phone number']
        row['Comments']
        """
        print(f'\tEntering form data for name: {row["Name"]}.')

        with Browser() as browser:  # Instiantiate a browser (will use Firefox as a default)
            # Go to the form
            browser.visit(form_url)  # Instruct the browser to visit the form

            # Enter data
            browser.find_by_name('entry.2005620554').fill(row['Name'])  # Find the name field by its input element name and enter data
            browser.find_by_name('entry.1045781291').fill(row['Email'])  # Find the email address field by its input element name and enter data
            browser.find_by_name('entry.1065046570').fill(row['Address'])  # Find the address field by its input element name and enter data
            browser.find_by_name('entry.1166974658').fill(row['Phone number'])  # Find the phone number field by its input element name and enter data
            browser.find_by_name('entry.839337160').fill(row['Comments'])  # Find the comments field by its input element name and enter data

            # Submit the form
            browser.find_by_xpath('//content/span[contains(@class, "quantumWizButtonPaperbuttonLabel")]').click()  # Find the submit button and click it

        line_count += 1  # Increment line counter
    print(f'Processed {line_count} lines.')
