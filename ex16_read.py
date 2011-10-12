print "Type a file name to read"

file = raw_input ("> ")

txt = open(file)

print "And now I will read %r ." % file
print txt.read()

print "Close the %r" % file
txt.close()
