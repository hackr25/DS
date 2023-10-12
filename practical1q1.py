#Q.1) Write a program to demonstrate the use of various Data Types and Structures in python


a = 5  
print("The type of a ", type(a))    
b = 40.5  
print("The type of b ", type(b))   
c = 1+3j  
print("The type of c ", type(c))  


str = " string using double quotes " 
print(str)  


list1  = [1, "hi", "Python", 2]    
  
print(type(list1))  
  

print (list1)  
  

print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)


tup  = ("hi", "Python", 2)    

# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)


d = {1:"Jimmy", 2:"Alex", 3:"john", 4:"mike"}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is"+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())
