# The data we need to retrieve - we are telling it to retrieve this named file from th resources folder that is inside the same folder as this file
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.-This is saving the file to a new analysis folder just created
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

        # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# 1. Total number of votes cast 
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
