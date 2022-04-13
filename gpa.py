classamt = int(input("How many classes do you have?> "))
points = 0

for classnum in range(0, classamt):
    points += int(input(f"Points for class {classnum + 1}> "))

print(f"Your GPA is: {round(points / classamt, 2)}")
