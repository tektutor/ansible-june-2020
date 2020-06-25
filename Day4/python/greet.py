#!/usr/bin/python

class Greeting:
   
   def __init__(self):
       print ("Greeting constructor ...")
       self.x = 0
       self.y = 0

   def setValues(self, value1, value2 ):
       self.x = value1
       self.y = value2

   def printValues(self):
       print ( 'X = ' + str ( self.x ) )
       print ( 'Y = ' + str ( self.y ) )

   def sayHello(self, msg):
       print ( 'Hello ' + msg )


obj1 = Greeting()
obj1.sayHello("Python !")
print('#Obj1 - Value of X & Y before set Values ...')
obj1.printValues()
print('#Obj1 - Value of X & Y after set Values ...')
obj1.setValues(10,20)
obj1.printValues()

obj2 = Greeting()
obj2.sayHello("Ansible !")
print('#Obj2 - Value of X & Y before set Values ...')
obj2.printValues()








