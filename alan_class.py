class Printer:
  def __init__(self,number=3):
     self.value = number
  def sayIt(self):
     print self.value

class MyApp:
  def __init__(self, aPrinter = None):
      if aPrinter == None:     # if no object passed create one
         aPrinter = Printer()
      self.obj = aPrinter      # assign object
  def doIt(self):
      self.obj.sayIt()         # use object

def test():
  p = Printer(42)
  a1 = MyApp()
  a2 = MyApp(p)   # pass p object into a2
  a1.doIt()   # prints default value = 0
  a2.doIt()   # prints 42, the value of p

test()

"""
We have a Printer class that prints numbers that are passed to it.
We have a MyApp class that 
"""
