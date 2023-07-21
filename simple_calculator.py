# This program is designed to be a calculator that prints the calculated amount according to the 
# specified inputs.
# The program will ask the user if it would like to input more data or if it would like to read the previous data inputted from 
# a text file.
# This program makes use of defensive programming.

print("Please enter two numbers and an operator (i.e. +,- etc.) below to form an equation.")
print()

while True:
    try:
        number_1 = int(input("First number: "))
        number_2 = int(input("Second number: "))
    except ValueError:
        print("This is not a valid number. Please try again.")
        continue
        

    operation = input("Operation: ")
    valid_operations = ['+', '-', '*', '/', '**','%']

    if operation == '+' and operation in valid_operations:
        plus = number_1 + number_2
        result = (f"{number_1} {operation} {number_2} = {plus}")
        print(result)
    elif operation == '-' and operation in valid_operations:
        minus = number_1 - number_2
        result = (f"{number_1} {operation} {number_2} = {minus}")
        print(result)
    elif operation == '*' and operation in valid_operations:
        multiply = number_1 * number_2
        result = (f"{number_1} {operation} {number_2} = {multiply}")
        print(result)
    elif operation == '/' and operation in valid_operations:
        if number_2 == 0:
            print('Error: You cannot divide by zero')
            continue
        divide = number_1/ number_2
        result = (f"{number_1} {operation} {number_2} = {divide}")
        print(result)
    elif operation == '**' and operation in valid_operations:
        power = number_1 ** number_2
        result = (f"{number_1} {operation} {number_2} = {power}")
        print(result)
    elif operation == '%' and operation in valid_operations:
        modulus = number_1 % number_2
        result = (f"{number_1} {operation} {number_2} = {modulus}")
        print(result)
    else:
        print("This is not a valid operator. Please try again.")
        continue
        
    with open('equations.txt', 'a+') as file:
        file.write(result + '\n')

    print()
    new_input = input('''If you'd like to input another equation please input 'Yes'. If you'd like to read the previous equations
please input 'No' and then the file name 'Equations'. \n''').lower()
    print()

    if new_input == 'yes':
        continue
    elif new_input == 'no':
        new_file = input("Enter the file name: ")
        if new_file == 'equations':
            try:
                with open('equations.txt', 'r') as f:
                    lines = f.read()
                    print(lines)
                    break
            except FileNotFoundError:
                print('This equations file does not exist.')
        else:
            print("This file name is invalid. Try again.")
    else:
        print('This input is invalid. Please try again.')
    
        