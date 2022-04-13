points = 0
classamt = int(input("How many classes do you have?> "))



print("First Quarter")
for classnum in range(0, classamt):
    points += int(input(f"Points for class {classnum + 1}> "))
q1 = points

print("Second Quarter")
points = 0
for classnum in range(0, classamt):
    points += int(input(f"Points for class {classnum + 1}> "))
q2 = points

print("Third Quarter")
points = 0
for classnum in range(0, classamt):
    points += int(input(f"Points for class {classnum + 1}> "))
q3 = points

print("Fourth Quarter")
points = 0
for classnum in range(0, classamt):
    points += int(input(f"Points for class {classnum + 1}> "))
q4 = points

avgq1 = round(q1 / classamt,2)
avgq2 = round(q2 / classamt,2)
avgq3 = round(q3 / classamt,2)
avgq4 = round(q4 / classamt,2)

avgsem1 = round((avgq1 + avgq2) / 2,2)
avgsem2 = round((avgq3 + avgq4) / 2,2)

finalavg = round((avgsem1 + avgsem2) / 2,2)

print(f"Q1 GPA: {avgq1}\nQ2 GPA: {avgq2}\nQ3 GPA: {avgq3}\nQ4 GPA: {avgq4}\nSemester 1 GPA: {avgsem1}\nSemester 2 GPA: {avgsem2}\nFinal GPA: {finalavg}")
