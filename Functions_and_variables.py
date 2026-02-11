# x = 9999
# y = 1
# z = x + y

# print(f"{z:,}")

# a = 2
# b = 3
# c = a / b

# print(f"{c:.2f}")



def meet_the_user(): 
    AI_name = "Molly"
    user_name = input("""Welcome to Basic Arithmetic Calculator
Kindly enter your name for identification purpose: """)                                                    
    user_name = user_name.capitalize()
    response = f"""\nHello {user_name} my name is {AI_name}. 
I'm an AI created to perform basic math operations
Kindly enter the numbers you'll like to perform an operation on

    """
    print(response)

def user_input():
    num1 = int(input("Enter first digit: "))
    num2 = int(input("Enter second digit: "))

    return num1, num2 

def user_options():
    options = ["Addition", "Subtraction", "Multiplication", "Division"]
    print("Select an Operation", end = 2 * "\n")
    for index, option in enumerate(options, 1):
        print(f"Enter {index} for {option}")
    

def operations(option, num1, num2):
    status = True

    while status:
        if option == 1:
            return num1 + num2
        elif option == 2:
            return num1 - num2
        elif option == 3:
            return num1 * num2
        elif option == 4:
            return num1 / num2
        else:
            print("Invalid input, Try again")
           
    
def calculator():
    print(f"\nResult is {result}")


meet_the_user()
num1, num2 = user_input()
user_options()
option = int(input(": "))
result = operations(option, num1, num2)
calculator()

