for x in range(151):
    print(x)


for x in range(5, 1001, 1):
    if x % 5 == 0:
        print(x)


for x in range(1, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    if x % 5 == 0:
        print("Coding")
    else:
        print(x)

sum = 0
for x in range(0, 500001, 1):
    if x % 2 != 0:
        sum = sum + x
    if x == 500000:
        print(sum)


for x in range(2018, 0, -4):
    print(x)


lowNum = 5
highNum = 30
mult = 7
for x in range((lowNum), (highNum), 1):
    if x % (mult) == 0:
        print(x)

