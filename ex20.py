# import some functionality
from sys import argv

# unpack the argv that takes two values scipt and input file
script, input_file = argv

# define print_all that has one argument - f.  Print_all prints the contents of the input file
def print_all(f):
    print f.read()

# define rewind that has one argument - f.  Rewind moves the reading cursos to the beginning of the file
def rewind(f):
    f.seek(0)

# define print_a_line that takes two arguments -line_count and and f.  
# Print_a_line prints a line number of the input file and the contents of that line
def print_a_line(line_count, f):
    print line_count, f.readline()

# Create a variable current_file that opens the input_file 
current_file = open(input_file)

# Print out a description of what will appear on the screen
print "First let's print the whole file: \n"

# Run print_all function on the current_file
print_all(current_file)

# Print out a description what what will be done next
print "Now let's rewind, kind of like a tape."

# Run the rewind function on the current_file to take the curser to the beginning
rewind(current_file)

# Print out what will appear on the screen next
print "lets print three lines: \n"

# Set current_line to 1
current_line = 1
# Run print_a_line function with current_line and current_file that displays the line number and the text of the line
print_a_line(current_line, current_file)

# Set current_line to what it was plus one line
current_line += 1
# Run print_a_line function with current_line and current_file that displays the line number and the text of the line
print_a_line(current_line, current_file)

# Set current_line to what it was plus one line
current_line += 1
# Run print_a_line function with current_line and current_file that displays the line number and the text of the line
print_a_line(current_line, current_file)
    
