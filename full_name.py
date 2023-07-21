# This program is created to perform a full name check.

print("Please enter your full name below.")

name = input("Name:")
surname = input("Surname:")

full_name = name + surname

# An if-elif-else control structure is designed to ensure
# a full name is entered

if len(full_name) <= 4: 
    print("You have entered less than four characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
