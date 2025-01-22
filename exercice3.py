print("This program calculates the area of a cut disk")
rEXT = float(input("Enter the radius of the outer disk: "))
rINT = float(input("Enter the radius of the inner hole: "))

if rEXT > rINT:
    s = (rEXT**2 * 3.14) - (rINT**2 * 3.14)
    print("The area of the cut disk is:", s)
    input()
else:
    print("Error")
    input()
