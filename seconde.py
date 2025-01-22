def user_input():
    print("1-Addistion")
    print("2-Subtract")
    print("3-Multiply")
    print("4-Divide")
    try:
        user = int(input("Enter what you want? "))
    except ValueError:
        print("give a number betwen 1 and 5")
    
    if user == 1:
        addition()
    elif user == 2:
        subtract()
    elif user == 3:
        multiply()
    elif user == 4:
        divide()
    else:
        print("Choose a correct number")
        user_input()


def addition():
    print("Give us two numbers to add")
    try:
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))
        add = numb1 + numb2
        print(f"The solution of {numb1} + {numb2} is {add}")
        user_input()
    except ValueError:
        print("Give a real number please")
        addition()


def subtract():
    print("Give us two numbers to subtract")
    try:
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))
        sub = numb1 - numb2
        print(f"The solution of {numb1} - {numb2} is {sub}")
        user_input()
    except ValueError:
        print("Give a real number please")
        subtract()


def multiply():
    print("Give us two numbers to multiply")
    try:
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))
        mult = numb1 * numb2
        print(f"The solution of {numb1} × {numb2} is {mult}")
        user_input()
    except ValueError:
        print("Give a real number please")
        multiply()


def divide():
    print("Give us two numbers to divide")
    try:
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))
        if numb2 != 0:
            div = numb1 / numb2
            print(f"The solution of {numb1} ÷ {numb2} is {div}")
        else:
            print("Cannot divide by zero!")
        user_input()
    except ValueError:
        print("Give a real number please")
        divide()


user_input()
