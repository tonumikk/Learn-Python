def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d /%d" % (a, b)
    return a /b 


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it my hand?"

# Figuring out the puzzle
# First we add two values age and the other value

divide1 = divide(iq, 2)
multiply1 = multiply(weight, divide1)
subtract1 = subtract(height, multiply1)
what_new = add(age, subtract1)
print "Let's see if this does it: ", what_new

# Let's create a different formula ... Let's make it height divided by age plus weight
new_what = add(divide(height, age), weight)

print "Let's now print the new formula: ", new_what
