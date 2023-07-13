import os
import csv

#This will allow us to create file paths across operating systems
csvpath = os.path.join('..','Resources','election_data.csv')

# Function to analyse poll data
def analyse_poll_data(data):
    total_votes = 0
    candidates = {}
    
    for row in data:
        # Count total votes
        total_votes = total_votes + 1

        # Count votes for each candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    
    # Find the winner based on popular vote
    winner = max(candidates, key=candidates.get)

    # Calculate the percentage of votes for each candidate
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Print the analysis
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export the analysis to a text file
    with open('election_results.txt', 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")


# Read the poll data from CSV
with open(csvpath) as file:
    csv_reader = csv.reader(file)
    # Skip the header row
    header = next(csv_reader)
    # Pass the remaining rows to the analysis function
    analyse_poll_data(csv_reader)
