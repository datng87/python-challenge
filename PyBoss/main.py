import os
import csv
from posixpath import split
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
EmpId =[]
firstName =[]
lastName =[]
dob=[]
ssn =[]
stateShort=[]

inputpath = os.path.join("Resources",'employee_data.csv')


with open (inputpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        EmpId.append(row[0])
        fullname = row[1].split(" ")
        firstName.append(fullname[0])
        lastName.append(fullname[1]) 
        dobori = row[2].split("-")
        dob.append(dobori[2]+"/"+dobori[1]+"/"+dobori[0])
        ssnori = row[3].split("-")
        ssn.append("***-**-"+ssnori[2])
        stateShort.append(us_state_abbrev[row[4]])

myheader =["Employee ID","First name","Last name","DOB","SSN","State"]
outdata = zip(EmpId,firstName,lastName,dob,ssn,stateShort)         

#write to result.csv
outputfilepath = os.path.join ("analysis","result.csv")

with open (outputfilepath, "w",newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(myheader)
    csvwriter.writerows(outdata)
