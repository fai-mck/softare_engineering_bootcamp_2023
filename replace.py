# This program prints the below sentence in different ways.
sentence = ("The!quick!brown!fox!jumps!over!the!lazy!dog!.")

# The string manipulation below prints the sentence without the '!'.
print (sentence.replace("!"," "))

# The string manipulation below prints the sentence without the '!' and 
# in all capitals.
print (sentence.replace("!"," ").upper())

#The string manipulation below prints the sentence in reverse.
print (sentence[::-1])
