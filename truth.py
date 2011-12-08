""" Programmatic way to Truth Tables """

print "These exercises will test you how well you know the truth tables"
print "The computer asks you a question and you need to enter 'True' or 'False'"

print "What is 'not False'"
answer = raw_input("Type your answer: ")

if answer == "True":
    print "Correct - good job!";
else: 
    print "Incorrect - try again."

print "What is 'not True'"
answer = raw_input("Type your answer: ")
if answer == "False":
    print "Correct - good job!";
else: 
    print "Incorrect - try again."


