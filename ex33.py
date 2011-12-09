print "First the while loop..."

def while_loop(i, some_number, incrementor):
    numbers = []
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

print "_______________________________________"
raw_input("Press Enter to continue...")
print "And now the same with the for loop :-)."

def for_loop(i, some_number):
    numbers2 = []
    incrementor = 2
    for i in range(i, some_number, incrementor):
        print "At the top i is %d" % i
        numbers2.append(i)

        print "numbers now: ", numbers2
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers2:
        print num

for_loop(0, 10)
