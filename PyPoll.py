#importing election_results.csv file
#created a new folder called 'Resources'
#three columns: Ballot ID, County, and Candidate, no. of rows 369711(excl. header)
# Task: 1. Total number of votes cast, 2. A complete list of candidates who received votes
 # 3.Total number of votes each candidate received, 4.Percentage of votes each candidate won, 5.The winner of the election based on popular vote

#"r": Open a file to be read.
#"w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
#"x": Open a file for exclusive creation. If the file does not exist, it will not create one.
#"a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
#"+": Open a file for reading and writing.
import csv
#The os module allows us to interact with our operating system. Give us access to indirect path 
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.

    #print the header row
    headers = next(file_reader)
    print(headers)

#    for row in file_reader:
#        print(row[0]) # to print the first item from each row)
#Close the file
#election_data.close()


#-------------------------WRITING A FILE---------------------------------------#
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
#    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")    # use of \n for newline

# Close the file
#file_to_load.close()