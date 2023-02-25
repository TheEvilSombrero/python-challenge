#Import libraries 
import os, csv

#set up file path 
csvPath = os.path.join("budget_data.csv")

#variables to store data in 
time = []
lengthOfTime = 0
totalMoney = []
total = 0
averageChange = 0.0
maxChange = 0.0
minChange = 0.0
maxChangeDate = str()
minChangeDate = str()

#open up CSV
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    csvHeader = next(csvFile)

#    print(csvHeader)
    
    #getting length of time in months 
    for rows in csvReader:
        time.append(rows[0])
        lengthOfTime = len(time)
    
    #getting net total of profit/losses over time period 
        totalMoney.append(int(rows[1]))
        total = sum(totalMoney)
        total = format(total, ',.2f')

    #Average change (change in profit/loss over time, then average of those changes)
    #Sum of total / length of total 
        averageChange = (sum(totalMoney)/len(totalMoney))
        averageChange = format(averageChange, ',.2f')

    #Greatest increase in profits - month and year, ammount decrease 
    #find row[1] w/ the highest value, print row[0] w/ row[1]
        maxChange = max(totalMoney)
        if maxChange == int(rows[1]):
            maxChangeDate = str(rows[0])
        maxChange = format(maxChange, ',.2f')

    #Greatest decrease in profits - month and year, ammount decrease 
    #find row[1] w/ lowest value, print row[0] w/ row[1]
        minChange = min(totalMoney)
        if minChange == int(rows[1]):
            minChangeDate = str(rows[0])
        minChange = format(minChange, ',.2f')

    #Printing all of the information in the terminal 
    print("--Financial Analysis--")
    print("-------------------------")
    print(f"Total Months: {lengthOfTime}")
    print(f"Net total of profits/losses: ${total}")
    print(f"Average change of profits/losses: ${averageChange}")
    print(f"Greatest increase in profits: ({maxChangeDate}) ${maxChange}")
    print(f"Greatest decrease in profits: ({minChangeDate}) ${minChange}")
    print("-------------------------")

    #Defining file path for output text file 
    PyBankOutput = os.path.join("PyBankOutput.txt")
    
    #Creating new text file to output the data 
    outputTXT = open(PyBankOutput, 'w')

    #Writing all of the data on new lines 
    outputTXT.write("--Financial Analysis--\n")
    outputTXT.write("-------------------------\n")
    outputTXT.write(f"Total Months: {lengthOfTime}\n")
    outputTXT.write(f"Net total of profits/losses: ${total}\n")
    outputTXT.write(f"Average change of profits/losses: ${averageChange}\n")
    outputTXT.write(f"Greatest increase in profits: ({maxChangeDate}) ${maxChange}\n")
    outputTXT.write(f"Greatest decrease in profits: ({minChangeDate}) ${minChange}\n")
    outputTXT.write("-------------------------\n")

    #closing the text file 
    outputTXT.close()