import random
from time import sleep

file='tokens.txt'
timedelay=60 #Set delay in seconds

while True:
    print(f"{file} is getting shuffled.\n")
    lines = open(file).readlines()
    random.shuffle(lines)
    open(file, 'w').writelines(lines)
    print(f'{file} is done getting shuffled.\n')
    sleep(timedelay)
