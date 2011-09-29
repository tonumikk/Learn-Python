print "Type a file name to open: " 
filename = raw_input('> ')

# Define a variable for opening a file
txtopen = open(filename)

print txtopen.read()

