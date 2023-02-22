#Import libraries 
import os, csv

#set up file path 
csvPath = os.path.join("election_data.csv")

#initialize variables 
rowCopy = []
totalVotes = 0
candidates = []
candidatesAndVotes = {}
vote0 = 0
vote1 = 0
vote2 = 0
votes = []
percent0 = 0.0
percent1 = 0.0
percent2 = 0.0
percentVotes = []

#open csv
with open(csvPath, "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    csvHeader = next(csvFile)

#    print(csvHeader)

#Start for loop to iterate through CSV 
    for rows in csvReader:

        #find total number of votes 
        rowCopy.append(rows)
        totalVotes = len(rowCopy)

        #create list of candidates - if rows[2] not in list add to the list 
        if rows[2] not in candidates:
            candidates.append(rows[2])

        #conditionals to count votes per candidate 
        #Only works with <= 3 candidates - would improve in 2.0
        if candidates[0] == rows[2]:
            vote0 += 1
        elif candidates[1] == rows[2]:
            vote1 += 1
        elif candidates[2] == rows[2]:
            vote2 += 1
      
        #calculating percentage of votes for each candidate 
        percent0 = (vote0/totalVotes)*100
        percent1 = (vote1/totalVotes)*100
        percent2 = (vote2/totalVotes)*100

    #formatting all of the calculated values 
    totalVotes = format(len(rowCopy), ',')
    vote0 = format(vote0, ',')
    vote1 = format(vote1, ',')
    vote2 = format(vote2, ',')
    percent0 = format(percent0, ',.3f')
    percent1 = format(percent1, ',.3f')
    percent2 = format(percent2, ',.3f')

    #printing election results as shown in readme
    print("--Election Results--")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    print(f"{candidates[0]}: {percent0}% ({vote0} Votes)")
    print(f"{candidates[1]}: {percent1}% ({vote1} Votes)")
    print(f"{candidates[2]}: {percent2}% ({vote2} Votes)")
    print("-------------------------")
    print(f"Winner: {candidates[1]}")
    print("-------------------------")

    #defining file path for output file 
    PyPollOutput = os.path.join("PyPollOutput.txt")

    #Creating new text file to output the data 
    outputTXT = open(PyPollOutput, 'w')

    #Writing all of the info on new lines 
    outputTXT.write("--Election Results--\n")
    outputTXT.write("-------------------------\n")
    outputTXT.write(f"Total Votes: {totalVotes}\n")
    outputTXT.write("-------------------------\n")
    outputTXT.write(f"{candidates[0]}: {percent0}% ({vote0} Votes)\n")
    outputTXT.write(f"{candidates[1]}: {percent1}% ({vote1} Votes)\n")
    outputTXT.write(f"{candidates[2]}: {percent2}% ({vote2} Votes)\n")
    outputTXT.write("-------------------------\n")
    outputTXT.write(f"Winner: {candidates[1]}\n")
    outputTXT.write("-------------------------\n")

    #closing text file 
    outputTXT.close()