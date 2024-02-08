class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):    
    '''метод класса,выводящий имя объекта'''
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
