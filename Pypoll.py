# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote.

import csv
import os
# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save a file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes ={}
# winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader (election_data)

    # Read the Header row.
    Headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrive vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # Print the candidate name and percentage of votes.
    print(f"{candidate}: received {vote_percentage: .1f}% of the vote.")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate
# Print out each candidate's name, vote count, and percentage of votes 
print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-------------------------------\n")
print(winning_candidate_summary)
# Print the total votes
#print (total_votes)
# Print the candidate list.
#print(candidate_options)
# Print the candidate vote dictionary
#print(candidate_votes)

    
   
    





