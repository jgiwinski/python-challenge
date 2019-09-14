# import all the things! 
import os
import pandas as pd 
import numpy as np 
import csv 

# declare the dictionary
candidateDict = {}

# declare all the variables
totalvotes = 0
lineBreak = "-"*30

# path to all the things
voter_csv = os.path.join('election_data.csv')

with open(voter_csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')  
    next(reader)
    # find all the data things 
    for row in reader:
        # keep a running total of all votes
        totalvotes += 1

        # count votes for each specific candiate using their name as the key
        if row[2] not in candidateDict: 
            candidateDict[row[2]] = 0 
        candidateDict[row[2]] += 1
    #print(candidateDict)

    # find and print the name, vote percent, and total votes 
    for name, votes in candidateDict.items():
        vote_percent = votes / totalvotes


with open ("pollFile.txt", 'w') as f: 
    f.write(f"Election Result\n")
    f.write(f"{lineBreak}\n")
    f.write(f"Total Votes: {totalvotes}\n")
    
    for key,value in candidateDict.items():
        print(key,"  ", str(round((value/totalvotes)*100,2)),"% ", value)
        f.write(f"{key}: {round((value/totalvotes)*100,2)}% ({value})\n")

    f.write(f"{lineBreak}\n")
    f.write(f"Winner:{max(candidateDict, key=candidateDict.get)}\n")




