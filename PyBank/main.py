import os
import csv
maxVar = 0
minVar = 0
mycount = 0
mysum = 0
prevalue = 0
sumvar = 0
profit =[]
profitvariance =[]
inputpath = os.path.join("Resources",'budget_data.csv')

with open (inputpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        mycount +=1     #count number of month
        mysum += int(row[1])        #net sum profit
        if mycount ==1:     #if first line
            prevalue = int(row[1])      
        else:       #subsequence lines
            if (int(row[1]) - prevalue) > maxVar:   #variation is max
                maxVar = int(row[1]) - prevalue
                monthmaxVar = row[0]
            elif (int(row[1]) - prevalue) < minVar:     #variation is min
                minVar = int(row[1]) - prevalue  
                monthminVar = row[0]      
            sumvar += int(row[1])-prevalue  #net sum variation
            prevalue = int(row[1])
            
averagevar = round(sumvar / (mycount-1),2)  #average variation
#write to result.txt
outputfilepath = os.path.join ("analysis","result.txt")

with open (outputfilepath, 'w') as f:
    f.write ("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months:" + str(mycount) + "\n")
    f.write ("Total: $"+str(mysum)+"\n")
    f.write ("Average  Change: $"+str(averagevar)+"\n")
    f.write ("Greatest Increase in Profits: "+ monthmaxVar+" ($"+  str(maxVar)+")\n")
    f.write ("Greatest Decrease in Profits: "+ monthminVar+" ($"+  str(minVar)+")\n")

#print to terminal
print("Financial Analysis")
print("----------------------------")
print (f"Total Months: {mycount}")
print (f"Total: ${mysum}")
print (f"Average  Change: ${averagevar}")
print ("Greatest Increase in Profits:", monthmaxVar,"($",  maxVar,")"  )
print ("Greatest Decrease in Profits:", monthminVar,"($",  minVar,")"  )