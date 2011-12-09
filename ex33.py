# i = 0 
numbers = []

def while_loop(i, some_number, incrementor):
    while i < some_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incrementor
        print "numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_loop(0, 10, 2)
