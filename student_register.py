# This program creates a student register for an exam venue by using external data sources in the form of output.
# Each student registering will be asked for their student ID number which will be written to a text file that displays
# their student ID number and allows a space below to sign for their attendance. 

with open('reg_form.txt', 'a') as register:

    stu_amount = int(input("How many students will be registering for this exam venue? "))

    for amount in range(stu_amount):
        stu_i_d = int(input("Please enter your 9 digit student ID number: "))
        register.write(str(stu_i_d) + ' ' + '\n........................' + '\n')

