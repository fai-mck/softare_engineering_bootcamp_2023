# This program allows the user to input any amount
# of numbers until the user enters -1.
# Once -1 has been entered, the program will calculcate the average 
# of the numbers entered excluding -1.

total_inputs = 0    # To calculate the amount of inputs NOT the sum of all inputs.
add_inputs = 0      # To calculate the sum of all inputs.

number = int(input("Please enter a number: "))

while number != -1:
    total_inputs += 1
    add_inputs += number
    
    print('If you would like to exit the application, please enter -1.')
    number = int(input("Please enter a number: "))
    
    if number == -1:
        average = add_inputs/ total_inputs
        print (average)
        break



