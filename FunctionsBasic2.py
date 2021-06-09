# Countdown
def countdown(num):
    new_list = []
    for x in range(num, -1, -1):
        new_list.append(x)
    return new_list
print(countdown(5))

#PrintAndReturn
def printReturn(numList):
    print(numList[0])
    return numList[1]
print(printReturn([22,23]))

#FirstPlusLength
def FirstPlusLength(numList):
    return numList[0] + len(numList)
print(FirstPlusLength([1,2,14,17,22]))

#ValuesGreaterThanSecond
def ValuesGreaterThanSecond(firstList):
    secondList = []
    second_value = firstList[1]
    for x in range(len(firstList)):
        if firstList[x] > second_value:
            secondList.append(firstList[x])
    print(len(secondList))
    return secondList

print(ValuesGreaterThanSecond([5,3,2,1,7,8,11]))

#ThisLengthThatValue
def LengthValue(size, value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList
print(LengthValue(5,22))