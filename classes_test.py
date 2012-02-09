# Python classes

class PythonClass(object):
    def __init__(self, number):
        self.value1 = number

class PythonClass2(object):
    # Do something
    def do_something(self, number):
        print number + 15

f = PythonClass(3)
b = PythonClass2()
# I'm using the variable from one instance in another!
b.do_something(f.value1)

    
