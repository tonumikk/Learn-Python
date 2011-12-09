#i = 0 
numbers = []
some_number = 12

def while_loop(i):
    while i < some_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_loop(0)
