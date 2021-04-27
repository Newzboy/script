from random import randint

sel = int(input('How many numbers should be generated? '))
rng = int(input('What should the range of the numbers be? (0 to input) '))
num = 0

while num in range(0,sel):
    print(str(randint(1,rng)))
    num = num + 1
