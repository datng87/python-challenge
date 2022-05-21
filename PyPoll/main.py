import os
import csv

numCandidate =0
voteCount =0
votePercent =0.0
inputpath = os.path.join("Resources",'election_data.csv')
voteResult = {"candidate":[],
              "vote":[]}

with open (inputpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        voteCount +=1     #count the vote
        if numCandidate == 0:   #enter first data for first line
            voteResult["candidate"].append(row[2])
            voteResult["vote"].append(1)
            numCandidate +=1
        else:
            for i in range(numCandidate):   #check if there is a new candidate
                if row[2] == voteResult["candidate"][i]:    #if the line matches old candidate
                    voteResult["vote"][i] +=1       #increase the vote of the matched candidate
                    break
                elif row[2] != voteResult["candidate"][i] and i == (numCandidate -1):   # Candidate is new (last candidate not matches the line)
                    voteResult["candidate"].append(row[2]) 
                    voteResult["vote"].append(1)
                    numCandidate +=1
                
#find the winner
winnerIndex = voteResult["vote"].index(max(voteResult["vote"]))
winner = voteResult["candidate"][winnerIndex]

#write to result.txt
outputfilepath = os.path.join ("analysis","result.txt")
with open (outputfilepath, 'w') as f:
    f.write ("Election Results\n")
    f.write("----------------------------\n")
    f.write("Total Votes: " + str(voteCount) + "\n")
    f.write("----------------------------\n")
    for x in range(numCandidate):
        votePercent = voteResult["vote"][x]*100/voteCount
        votePercentFormat = "{:.3f}".format(votePercent)
        f.write(voteResult["candidate"][x] + ": " + votePercentFormat +"% ("+str(voteResult["vote"][x])+")\n")
    f.write("----------------------------\n")
    f.write("Winner: " + winner +"\n")
    f.write("----------------------------\n")
#print to terminal
print("Election Results")
print("----------------------------")
print (f"Total Votes: {voteCount}")
print("----------------------------")
for x in range(numCandidate):
        votePercent = voteResult["vote"][x]*100/voteCount
        votePercentFormat = "{:.3f}".format(votePercent)
        print(voteResult["candidate"][x] + ": " + votePercentFormat +"% ("+str(voteResult["vote"][x])+")")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")