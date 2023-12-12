word_check = input("Insert the word you want to check for palindrome: ")
word_check = word_check.lower()
#slicing the word using indexing
backward = word_check[::-1]
#The first : start index, the next : end index, -1 getting the last char
if word_check == backward:
    print("Palindrome")
else:
    print("Not palindrome")
