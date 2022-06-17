# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Assign a variable for the file to load and the path
file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: perform analysis
    print(election_data)

#Add our dependenceies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Create candidate list
candidate_options = []

#1. Declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes +=1

        #Print the candidate name from each row
        candidate_name = row[2]
        #If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking the candidates vote
            candidate_votes[candidate_name]=0
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
    
    #Iterate through candidate list.
    for candidate_name in candidate_options:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/ float(total_votes) * 100
        # Print candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Determine the winning vote count and candidate
#Determine if the votes are greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true than set winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count=votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



    





 
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in Election\n-----------------\nArapahoe\nDenver\nJefferson")


