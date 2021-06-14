#Selection Sort
Arr = [-64, 25, -12, 22, 11]

for x in range (len(Arr)):
    minx = x
    for i in range(x+1, len(Arr)):
        if Arr[minx] > Arr[i]:
            minx = i
    temp = Arr[x]
    Arr[x] = Arr[minx]
    Arr[minx] = temp

print(Arr)
