#Q1. Python hash() function example
# Calling function
result1 = hash(21) #integer value
result2 = hash(22.2) #decimal value
result3 = hash("javapoint") #string value
result4 = hash((1,2,22)) #tuple value

#Displaying Result
print(result1)
print(result2)
print(result3)
print(result4)

#Q2. Customer
class Customer:
    def __init__(self,value):
        self.value = value
    def __hash__(self):
        return hash(self.value)

alice = Customer(1000)
bob = Customer(1000)
print(alice==bob)
print(alice is bob)
print(hash(alice)==hash(bob))

#Q3.Passing new custom object to the function
class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email

student = Student("Arun","arun@abc.om")

#Calling function
result = hash(student)
#Displaying Result
print(result)
