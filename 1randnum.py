from random import randint

number = randint(1,100000)

print(number)

f = open("numbers.txt", "a")
f.write(number)
f.close()
