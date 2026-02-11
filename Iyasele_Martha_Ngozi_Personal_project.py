AI_name = "Molly"
user_name = input("""Welcome to Basic Arithmetic Calculator

Kindly enter your name for identification purpose: """)

response = f"""Hello {user_name.capitalize()} my name is {AI_name}, 
I'm an AI created to perform basic math operations

Kindly enter the numbers you'll like to perform an operation on
"""
print(response)

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

operations = ["Addition", "Subtraction", "Multiplication"]

print("\nSelect an operation", end = "\n")

for index, operation in enumerate(operations, 1):
    print(f"Enter {index} for {operation}")

choice = int(input("\nOperation: "))

def operation(num1, num2):
    if choice == 1:
        return f"Result is {num1 + num2}"
    elif choice == 2:
        return f"Result is {num1 - num2}"
    elif choice == 3:
        return f"Result is {num1 * num2}"
    else:
        return "Wrong entry, try again"
    
print(operation(num1, num2))
# ====================================================================


    