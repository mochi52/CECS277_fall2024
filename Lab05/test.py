
file = open("tasklist_test.txt", 'r')
list = []
numoftask = 0
for line in file:
    if line != "\n":
        numoftask +=1
    elif line == "\n":
        numoftask += 0
print(f"You have {numoftask} tasks.")

