# The below program is program 1.
# It converts each alternative letter to upper case and each other alternative letter 
# to lower case.
print("Program 1:")

sentence = ("This is a sentence.")
mixed_sentence = ""

for i in range(len(sentence)):
    if i % 2 == 1:
        mixed_sentence += sentence[i].upper()
    else:
        mixed_sentence += sentence[i].lower()

print(mixed_sentence)

# The below program is program 2.
# It converts each alternative word from the above string to lower and upper case.
print("Program 2:")

split_sentence = sentence.split()       # Split sentence to index words instead of characters.
jumbled_sentence = ""                   # Store new sentence

for j in range(len(split_sentence)):
    if j % 2 == 0:
        jumbled_sentence += " " + split_sentence[j].upper()
    else:
        jumbled_sentence += " " + split_sentence[j].lower()

final_sentence = ''.join(jumbled_sentence).strip()
print(final_sentence)

