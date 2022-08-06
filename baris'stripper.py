from os import system

global filenameRead
global filenameWrite
global systemCommand
filenameRead = "count.txt"
filenameWrite = "da3rnywordlist.txt"
systemCommand = "cls"


def stripLines(arrOfLines, ind):
    tempStr = arrOfLines[ind]
    tempStr = tempStr[8:len(tempStr)+1:1]
    return tempStr

with open(filenameRead, 'r', encoding='utf-8') as fpr:
    print("Reading lines...")
    readLines = fpr.readlines()
    lengthOfArr = len(readLines)
    print("Finished Reading Lines.")



with open(filenameWrite, 'w', encoding='utf-8') as fpw:
    for i in range(lengthOfArr):
        print("Writing lines: " + str(i+1) + " out of " + str(lengthOfArr))
        fpw.write(stripLines(readLines, i))
        system(systemCommand)
