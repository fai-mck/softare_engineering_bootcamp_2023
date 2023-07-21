import math
# This program is designed to calculate either interest on an investment or a monthly bond repayment,
# depending on which calculator the user decides to use. 

print("""Welcome to the financial calculators page. Here you will be able to calculate your interest income or interest expense
based on your chosen calculator.""")
print()

print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond       - to calculate the amount you'll have to repay on your home loan.")
print()

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
print()

if choice == 'investment':
    interest_type = input("Simple or compound interest?\n").lower()
    print()
    if interest_type == 'simple':
        deposit_amount = int(input("Enter your deposit amount: "))
        interest_rate = int(input("Enter the interest rate per annum: "))
        investment_period = int(input("Enter the invesment period in years: "))
        rate = interest_rate/100
        total_simple = deposit_amount*(1+rate*investment_period)
        interest_earned = total_simple - deposit_amount
        print()
        print(f"Your total invesment after {investment_period} years is {total_simple}.")
        print()
        print(f"Your total interest earned over the {investment_period} year period is {interest_earned}.")
    else:
        deposit_amount = int(input("Enter your deposit amount: "))
        interest_rate = int(input("Enter the interest rate per annum: "))
        investment_period = int(input("Enter the invesment period in years: "))
        rate = interest_rate/100
        total_compound = deposit_amount*math.pow((1+rate),investment_period)
        interest_earned_2 = total_compound - deposit_amount
        print()
        print(f"Your investment after {investment_period} years is {total_compound}.")
        print()
        print(f"Your total interest earned over the {investment_period} year period is {interest_earned_2}.")
elif choice == 'bond':                                                                     
        present_value = int(input("Enter the present value of the home: "))
        interest_rate = int(input("Enter the interest rate per annum: "))
        months = int(input("Enter the number of months you plan to take to repay the bond: "))
        rate = interest_rate/100 / 12
        repayment = (rate*present_value)/ (1-(1+rate)**(-months))
        print()
        print(f"Your repayment will be {repayment} per month.")
else:
    print("This input is invalid. Please run the program again.")
