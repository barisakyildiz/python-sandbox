from os import system
from time import sleep

global filenameRead
global filenameWrite
global systemCommand
filenameRead = "count.txt"
filenameWrite = "da3rnywordlist.txt"
systemCommand = "cls"


def stripLines(arrOfLines):
    for i in range(len(arrOfLines)):
        print("Stripping lines: " + str(i+1) + " out of " + str(lengthOfArr))
        tempStr = arrOfLines[i]
        tempStr = tempStr[8:len(tempStr)+1:1]
        arrOfLines[i] = tempStr
    print("Finished Stripping!")
    return arrOfLines

with open(filenameRead, 'r', encoding='utf-8') as fpr:
    print("Reading lines...")
    readLines = fpr.readlines()
    lengthOfArr = len(readLines)
    print("Finished Reading Lines.")
    sleep(1)



with open(filenameWrite, 'w', encoding='utf-8') as fpw:
    writeLines = stripLines(readLines)
    print("Writing lines...")
    fpw.writelines(writeLines)

for i in range(4):
    print("Program will terminate in: " + str(4-(i+1)))
    sleep(1)
