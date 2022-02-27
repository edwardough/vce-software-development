# A class is like a 'blueprint' or 'template' which can be re-used
class MyPerson():
    def __init__( self, name, height ):
        self.name = name
        self.height = height
    def __str__( self ):
        return f"Hello, my name is {self.name} and my height is {self.height}"
    def changeName( self, newName ):
        self.name = newName
    def reset( self, newName, newHeight ):
        self.name = newName
        self.name = newHeight

class Employee(MyPerson):
    def __init__(self, name, height, unionStatus, taxFileNumber):
        super().__init__(name, height)
        self.unionStatus = unionStatus
        self.taxFileNumber = taxFileNumber
    def __str__(self):
        return f"Hello, my name is {self.name} and my height is {self.height}\nMy TFN is {self.taxFileNumber} and my union status is: {self.unionStatus}"
    def changeUnionStatus(self):
        self.unionStatus = not self.unionStatus

# Here we're making two INSTANCES of the 'blueprint' MyPerson
p1 = MyPerson("Cameron",180)
p2 = MyPerson("James",72)
p3 = Employee("Edward",202,True,555999111)

# We can access properties in the class using the . operator
print(p1.name)
print(p3.name)

# We can also call functions that we've defined in the class
print(p1)
print(p2)
p1.changeName("Tony")
print(p1)
p3.changeUnionStatus()
print(p3)