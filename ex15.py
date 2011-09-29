# Import the argv module
from sys import argv

# Unpack the arguments into variables
script, filename = argv

# Define a variable for opening a file
txt = open(filename)

# Print out the filename
print "Here's your file %r:" % filename
# Print out the file content
print txt.read()

# Print some instructions
print "I'll also ask you to type it again:"
# Define file_again variable to prompt user for filename
file_again = raw_input ("> ")

# Define txt_again variable to open the file
txt_again = open(file_again)

# Print the file 
print txt_again.read()

