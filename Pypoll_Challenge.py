# Add our dependencies
import csv
import os
# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save a file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Dictionary and candidate votes.
candidate_options = []
candidate_votes ={}
# County Dictionary and County Votes.
county_lst = []
county_votes = {}
# Track the winning county,winning county vote and percentage.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0
# Track the winning Candidate , vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load,'r') as election_data:
    file_reader = csv.reader (election_data)
    # Read the Header row.
    Headers = next(file_reader)
    # Read each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the county name from each row 
        county_name = row [1]
        # If the county does not match any existing county, add the county to the list
        if county_name not in county_lst:
            # Add the county name to the county list.
            county_lst.append(county_name)
            #Begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] +=1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's vote count.
        candidate_votes[candidate_name] +=1
# Save the results to the text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"---------------------------\n"
        f"County Votes:\n")   
    print(election_results, end= "")
     #Save the final vote count to the text file.
    txt_file.write(election_results) 
    # Determine the percentage of votes for each county and iterate through the county list.
    for county in county_lst:
        # Retrive vote count of a county.
        countyvotes = county_votes[county]
        # Calculate the percentage of votes for each county.
        countyvote_percentage = int(countyvotes) / int(total_votes) * 100
        # Print the county name and percentage of votes.
        county_results = (f"{county}: {countyvote_percentage: .1f}% ({countyvotes:,})\n")
        print(county_results, end = "")
        #Save the county results to the text file.
        txt_file.write(county_results)
        # Determine winning county vote, winning county percentage and county name
        if (countyvotes > winning_county_votes) and (countyvote_percentage > winning_county_percentage):
            winning_county_votes = countyvotes
            winning_county_percentage = countyvote_percentage
            winning_county = county   
    # Print the winning county's results to the terminal.
    winning_county_summary = (
        f"-----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)
    # Determine the percentage of votes for each candidate and iterate through the county list.
    for candidate in candidate_votes:
        # Retrive vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_results, end = "")
        #Save the candidate results to the text file.
        txt_file.write(candidate_results) 
        # Determine winning vote count, winning percentage and candidate name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    
   
    





