"""Learning about Python Keywords, Data Types, String Escape Sequences, String Formats and Operators"""

# Keywords...
print "and"
print "And is used to tie together two expressions."
print "Example: "

age = 20
sex = "female"

young_female = age < 30 and sex == "female"

if young_female:
    print "young female"

#!/usr/bin/python

# sum.py

numbers = [22, 34, 12, 32, 4]
sum = 0

i = len(numbers)

print i

while (i != 0):
   i -= 1
   sum = sum + numbers[i]

print "The sum is: ", sum
