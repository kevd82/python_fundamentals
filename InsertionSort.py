arr = [9, 3, 78, 12, 76, 0, -2]

for x in range(1, len(arr)):
    temp = arr[x]
    prevx = x-1
    while prevx >= 0 and temp < arr[prevx]:
        arr[prevx + 1] = arr[prevx]
        prevx -= 1
        arr[prevx + 1] = temp

print(arr)
