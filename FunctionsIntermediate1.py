import random
def randInt(min=0, max=100):
        num = random.random() * (max - min) + min
        x = round(num)
        return x

print(randInt())
print(randInt(max=222))
print(randInt(min=77))
print(randInt(min=77, max=222))