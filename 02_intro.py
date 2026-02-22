# name = input("What is your name? ")
# age = input("How old are you? ")

# print("Nice to meet you,", name)
# print("You are", age, "years old.")



# name = input("What is your name? ")
# age = input("How old are you? ")
# print("Nice to meet you,", name, "You are", age, "years old.")

# age = int(input("How old are you? "))
# next_year = age + 1
# print ("Next year, you will be", next_year)
# print(type(age))

try:
    age = int(input("How old are you? "))
    next_year = age + 1
    print ("Next year, you will be", next_year)
except ValueError:
    print("Please enter a valid number for your age.")
