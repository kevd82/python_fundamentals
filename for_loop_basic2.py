#BiggieSize
def biggieSize(list):
    for x in range(len(list)):
        if list[x]>0:
            list[x] = "big"
    return list
    
#print(biggieSize([-1,2,3,-2]))

#CountPositives
def CountPositives(list):
    countPos=0
    for x in range(len(list)):
        if list[x] > 0:
            countPos += 1
    last_x = len(list)-1
    list[last_x] = countPos
    return list

#print(CountPositives([1,5,6,-1,-2,4,-8]))

#SumTotal
def sumList(list):
    sum=0
    for x in range(len(list)):
        sum += list[x]
    return sum

#print(sumListVals([1,22,4,9,17]))

#Average
def avgListVals(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
        avg = sum/len(list)
    return avg

#print(avgListVals([1,2,5,20,22]))

#Length
def Length(list):
    return len(list)

#print(Length([2,4,5,6,7]))

#Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for x in range(len(list)):
            if list[x]<min:
                min = list[x]
        return min

#print(minimum([3,2,6,1,8]))

#Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for x in range(len(list)):
            if list[x]>max:
                max = list[x]
        return max

#print(maximum([1,3,22,5,7]))

#UltimateAnalysis
def UltAn(list):
    sum = sumList(list)
    avg = avgListVals(list)
    min = minimum(list)
    max = maximum(list)
    len = Length(list)
    UltAnalysis = {
        "sumTotal":sum,
        "average":avg,
        "minimum":min,
        "maximum":max,
        "length":len
    }
    return UltAnalysis

#print(UltAn([1,4,7,8,22]))

#ReverseList
def RevList(list):
    for x in range(int(len(list)/2)):
        temp = list[len(list)-1-x]
        list[len(list)-1-x] = list[x]
        list[x] = temp
    return list

print(RevList([5,6,7,22,4,]))
