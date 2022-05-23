import os
import csv
import re
inputpath = os.path.join("Resources",'paragraph_1.txt')
totalchar = 0
totalword = 0
with open (inputpath, 'r', encoding="UTF-8") as f:
    paragraph = f.read()

sentence = re.split("(?<=[.!?])[ ]+", paragraph)
numsentence = len(sentence)
mywords = paragraph.split(" ")

for i in mywords:
    totalchar += len(i)
averageletter = round(totalchar/len(mywords),1)
averagesentence = round(len(mywords)/numsentence,1)

print ("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(mywords)}")
print(f"Approximate Sentence Count: {numsentence}")
print(f"Average Letter Count: {averageletter}")
print(f"Average Sentence Length: {averagesentence}")


#write to result.csv

outputfilepath = os.path.join ("analysis","result_paragraph_1.txt")

with open (outputfilepath, "w") as f:
    f.write("Paragraph Analysis\n")
    f.write("-----------------\n")
    f.write("Approximate Word Count: " + str(len(mywords))+"\n")
    f.write("Approximate Sentence Count: "+str(numsentence)+"\n")
    f.write("Average Letter Count: "+str(averageletter)+"\n")
    f.write("Average Sentence Length: "+str(averagesentence)+"\n")  

