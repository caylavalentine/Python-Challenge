import os
import csv

file_to_load = "PyPoll/Resources/election_data.csv"
total_votes = 0
candidate_list = []
total_for_candidates = {}
winner = ""
winning_count = 0
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    #skip header
    header = next(reader)
    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            total_for_candidates[candidate_name] = 0
        total_for_candidates[candidate_name] += 1
    print("Election Results") 
    print("-------------")   
    print(f"Total Votes: {total_votes}")  
    print("-----------")  
    for k,v in total_for_candidates.items():
        percentage_of_votes = v/total_votes * 100
        print(f"{k}: {percentage_of_votes}%")
        print(percentage_of_votes)
        if v > winning_count:
            winning_count = v 
            winner = k 
    print(total_votes)
    print(candidate_list)
    print(total_for_candidates)
    print(winner)




