class Foo(object):
    def __init__(self, var):
        self.var = var

class Bar(object):
    def do_something(self, var):
        print var*3

if __name__ == '__main__':
    f = Foo(3)
    b = Bar()
    # look, I'm using the variable from one instance in another!
    b.do_something(f.var)
