# PLEASE USE THIS PROGRAM IN CONJUNCTION WITH THE DOB.txt FILE.
# This program is designed to read the contents of the DOB.txt
# file and arrange the information under the headings 'Name' and 'Birthdate'.

text_file = open('DOB.txt', 'r')
lines = text_file.readlines()

print('Name:')
for line in lines:
    change = line.strip().split()
    name = f'{change[0]} {change[1]}'
    print(name)
print()

print('Birthdate:')
for line in lines:
    change = line.strip().split()
    birthdate = f'{change[2]} {change[3]} {change[4]}'
    print(birthdate)

text_file.close()


    
    
