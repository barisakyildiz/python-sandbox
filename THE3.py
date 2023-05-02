def getInputFromUser():
    library = []
    initialStr = input("Enter the library: ")
    initialList = initialStr.split(';')
    for book in initialList:
        temp = book.split(':')
        library.append(temp)
    minimumLimit = int(input("Enter a minimum page limit: "))
    holidayLength = int(input("Enter the holiday length in days: "))
    readingSpeed = input("Enter the reading speed for genres: ")
    initialList = readingSpeed.split(';')
    readingSpeed = []
    for speed in initialList:
        temp = speed.split(':')
        readingSpeed.append(temp)

    return library, minimumLimit, holidayLength, readingSpeed

def readOrDonate(library, minimumLimit, holidayLength, readingSpeed):
    donateList = []; notReadList = []; readListStr = []; readList = []; currentDay = 0
    for book in library:
        if holidayLength == 0:
            break
        elif holidayLength > 0:
            for genre in readingSpeed:
                if genre[0] == book[0]:
                    flag = 1
                    ind = readingSpeed.index(genre)
                    break
                else:
                    flag = 0
            if flag == 1:
                if int(book[2]) >= minimumLimit:
                    current = int(book[2]) /  int(readingSpeed[ind][1])
                    if current % 1 > 0:
                        currentDay = currentDay + 1 + int(current)
                        holidayLength -= currentDay
                    elif current % 1 == 0:
                        currentDay += int(current)
                        holidayLength -= currentDay
                    if holidayLength >= 0:
                        readList.append(book[2])
                        printStr = "{} finishes by day {}.".format(book[1], currentDay)
                        readListStr.append(printStr)
                elif int(book[2]) < minimumLimit:
                    notReadList.append(book[1])
            else:
                donateList.append(book[1])
    totalNumberPages = 0
    for bookPage in readList:
        totalNumberPages += int(bookPage)
    
    return totalNumberPages, readListStr, donateList, notReadList
    
                




def main():
    library, minimumLimit, holidayLength, readingSpeed = getInputFromUser()
    totalNumberPages, readListStr, donateList, notReadList = readOrDonate(library, minimumLimit, holidayLength, readingSpeed)
    
    if len(readListStr) > 0:
        print("\nBooks Read:")
        for i in range(len(readListStr)):
            print("{}. {}".format(i + 1, readListStr[i]))
        print("\nTotal number of pages read: {}\n".format(totalNumberPages))
    else:
        print("\nNo book to read!\n")
    
    if len(donateList) > 0:
        print("Books to donate:")
        for i in range(len(donateList)):
            print("{}. {}".format(i + 1, donateList[i]))
    else:
        print("No book to donate!\n")

if __name__ == '__main__':
    main()