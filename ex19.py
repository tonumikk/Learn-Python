# Define a function name "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "you have %d boxes of creackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket.\n"

# print instructions to the screen
print "We can just give the function numbers directly:"
# run the function with some numbers
cheese_and_crackers(20,30)

# print instructions to the screen
print "OR, we can use variables from our script:"
# create a variable
amount_of_cheese = 10
# create a variable
amount_of_crackers = 50 
# run the function with the variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print instructions to the screen 
print "We can even do math inside too:"
# run a function and do math within a function
cheese_and_crackers(10 + 20, 5 + 6)

# print an explanation to the screen
print "And we can combine the two, variables and math:"
# run the function with adding numbers to variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
    
