# This program is an email simulator which makes use of OOP.
# The program allows the user to read an email, view unread emails or 
# exit the program.

class Email:

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

def mark_as_read(email):
    email.has_been_read = True
    print(f'\nThis email sent by {email.email_address} is now marked as read.')

inbox = []

def populate_inbox():
    email1 = Email('munch@fruity.com', 'Welcome to Fruity!',
                   '''Welcome to Fruity! Thank you for your subscription
                   to our fruit delivery service. All our fruits are of the highest quality
                   and we look forward to hearing your feedback.
                   Happy Munching.
                   Kind regards,
                   The Fruity Team''')
    
    inbox.append(email1)

    email2 = Email('reminder@school.com', 'Your Task 3 is due soon',
                   '''Dear student,
                   This email serves as a reminder that your task 3 is due in 10 hours.
                   Please ensure your submission is timeous to avoid penalties.
                   Kind regards,
                   The Academic Team''')
    
    inbox.append(email2)

    email3 = Email('sarah@gmail.com', 'DADS BIRTHDAY',
                   '''Lucy,
                   This is your mother. Do not forget your fathers birthday this weekend.
                   Bring wine and a gift.
                   Love mum ''')
    
    inbox.append(email3)

populate_inbox()

def list_emails():
    for i, email in enumerate(inbox):
        print(i, email.subject_line)

def read_email():
    list_emails()
    print()

    selected_email = int(input("Which email would you like to read? "))
    print()

    if selected_email <= len(inbox):
        email = inbox[selected_email]

        print(f'Email: \t \t {email.email_address}')
        print(f'Subject: \t {email.subject_line}')
        print()
        print(email.email_content)
        print()
        mark_as_read(email)

    else:
        print('Invalid entry.')

    
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    if user_choice == 1:
        print()
        read_email()
        
    elif user_choice == 2:
        unread_emails = []

        for email in inbox:
            if not email.has_been_read:
                unread_emails.append(email)
        
        if unread_emails:
            print()
            print('Here is a list of your unread emails:')
            print()

            for email in unread_emails:
                print(email.subject_line)

        else:
            print()
            print('You have no uread emails.')

    elif user_choice == 3:
        print()
        print("Exiting emails.")
        exit()
      
    else:
        print()
        print("Oops - incorrect input.")



        


       










         

    
    
    
    





        