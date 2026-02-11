# while True:
#     n = int(input("Enter a positive number: "))
#     if n > 0:
#         break

# =============================================================================
def greeting():
    AI_name = "Molly"
    print("Welcome!!! \nFor professional use only, Kindly enter your name", end= "")
    name = get_name(": ")
    email = get_email("Enter your email: ")
    print(f"""\nHello {name} my name is {AI_name}. 
    I'm an AI created to take any request in absence of my Boss
    What can I do for you today please? """, end= "")
    input(": ")
    print("\nRight away!")


def get_name(prompt):
    while True:
        try:
            user_name = input(prompt)
            user_name = user_name.strip().capitalize().isalpha()
            if not user_name:
                raise ValueError("Invalid input! Enter letters only \nPlease try again")
            return user_name
        except ValueError as error:
            print(error)

def get_email(prompt):
    while True:
        try:
            user_email= input(prompt)
            user_email = user_email.strip().islower()
            if not user_email:
                raise ValueError("Invalid input! Email should be all lowercase \nPlease try again")
            return user_email
        except ValueError as error:
            print(error)

greeting()


# print("Right away!!!")

# =============================================================================================
# 
# def house():
    # name = str(input("What's your name? "))
    # name = name.capitalize()
    # match name:
    #     case "Harry":
    #         print(f"Welcome to Hargworts {name}, we have been expecting you", "Done!!! Bye for now", sep = 2 * "\n", end = 2 * "\n")
    #     case "Hermione" | "Ron":
    #         print(f"Welcome {name}, you belong in \"Gryffindor\"", end = 2 * "\n")
    #     case "Draco":
    #         print(f"Welcome {name}, you belong in \"Slytherine\"", end = 2 * "\n")
    #     case _:
    #         print("Unknown Candidate", "Next Candidate Please", end = 2 * "\n")

# def repeat():
#     while True:
#         house()
#         continue

# house()
# repeat()
# ==========================================================================================

