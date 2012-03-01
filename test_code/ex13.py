from sys import argv
 
first = raw_input("1st number: ")
second = raw_input("2nd number: ")
third = raw_input("3rd number: ")
 
first, second, third = argv
 
print "Pick 3 numbers"
print "1st choice:", first
print "2nd choice:", second
print "3rd choise:", third