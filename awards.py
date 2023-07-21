# This program is designed to determine the award a participant competing in a triathlon would receive
# based on their total time to complete the triathlon.

swimming_time = (int(input("Please enter your swim time in minutes:")))
cycling_time = (int(input("Please enter your cycle time in minutes:")))
running_time = (int(input("Please enter your run time in minutes:")))
print()
# Each variable has been cast as an integer to limit the input to numbers only.
# The program is not designed to cater for any decimals i.e. only whole numbers to be entered.

total_time = swimming_time + cycling_time + running_time

print("You have completed the triathlon in {} minutes.".format(total_time))
print()

# An if-elif-else control structure is designed to output the award achieved by the participant based on their total time in minutes.
if total_time <= 100: 
    print("You have been awarded Provincial Colours. Congratulations!")
elif total_time > 100 and total_time <= 105: 
    print("You have been awarded Provincial Half Colours. Well done!")
elif total_time > 105 and total_time <= 110: 
    print("You have been awarded Provincial Scroll. Good job!")
else: 
    print("You did not make it within the qualifying time to be granted an award. Keep trying. You'll get there.")
   


