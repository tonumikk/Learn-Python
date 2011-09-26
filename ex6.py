# Define x
x = "There are %d types of people." % 10
# Define binary
binary = "binary"
# Define do_not 
do_not = "don't"
# Define y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the variables
print x
print y

# Insert variabes into a sentence
print "I said: %r." % x
print " I also said: '%s'." % y

# Define hilarious
hilarious = False
# Define joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Insert a variable into another variable 
print joke_evaluation % hilarious

# Define w and e
w = "This is the left side of ..."
e = "a string with a right side."

# Show how two strings are added
print w + e
