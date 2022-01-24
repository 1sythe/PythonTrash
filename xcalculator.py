result = int(input("Result should be:  "))
num = 0
X = 0

while num != result:
    num = 2 * X + 4 
    X += 1
    if num == result:
        X -= 1
        print("X = " + str(X))
    elif num > result:
        print("Not Possible.")
        break
