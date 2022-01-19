result = int(input("Result should be:  "))
num = 0
X = 0

while num != result:
    num = 2 * X + 4  # <--- FORMULA HERE
    X += 1
    if num == result:
        X -= 1
        print("X = " + str(X))
    elif num > result:
        print("Not Possible.")
        break

# Python X in Formula calculator
# Where it says "FORMULA HERE" enter the Formula and replace your X with the X variable
# Made by kiisuhh#2750
#
# Example:
# 2 * x + 4 = 44
# now you want to know what x is
# if you want to find out with the program it should look like this where it says "FORMULA HERE":
# num = 2 * X + 4
# then if the result should be 44, x has to be 22 because 2 * 22 + 4 results 44.
# The program will calculate this without knowing what x is, and you only have to provide what the Result should be.
