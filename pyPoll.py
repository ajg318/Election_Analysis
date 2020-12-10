# # # The data we need to retrieve: 
# # # Total number of votes cast
# # # A complete list of candidates who received votes
# # # Total number of votes each candidate received
# # # Percentage of votes each candidate won
# # # The winner of the election based on popular vote

# # #assign a variable for the file to laod and the path
# # file_to_load = 'Resources\election_results.csv'

# # # Open the election results and read the file
# # with open(file_to_load) as election_data:

# #      # To do: perform analysis.
# #      print(election_data)

# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # # Write some data to the file.
#     # txt_file.write("Hello World")
#     # # Write three counties to the file.
#     # txt_file.write("\nArapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     # txt_file.write("\nCounties in the Election\n------------------------------------")
#     # txt_file.write("\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)
        # Print the header row.

