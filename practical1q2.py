#2) Write a Python program to demonstrate use of arrays and operations of arrays.

 # Creating array:
import array as ar
newarr = ar.array('d', [2.1, 4.5, 5.5])
print(newarr)

#Slicing python array:
import array as ar
newarr = ar.array('d', [2.1, 4.5,3.5,4.2,3.3, 5.5])
print("First element:", newarr[0])
print("Second element:", newarr[1])
print("Last element:", newarr[-1])
print(newarr[2:5]) # 3rd to 5th
print(newarr[:])   # beginning to end

# Length of array:
a = len(newarr)

#Changing Element:
import array as ar
num = ar.array('i', [1, 2, 3, 5, 7, 10])
num[0] = 0    
print(num) 

# Adding Element:

import array as ar
num = ar.array('i', [1, 2, 3])
ln=len(num)
print(ln) #length
num[0] = 0  #changing first element  
print(num)
num.append(4) #appending 4 to array
print(num)    
num.extend([5, 6, 7]) #extending numbers with 5,6,7
print(num)



# Insertion operation:

import array as ar
num = ar.array('i', [1, 2, 3, 5, 7, 10])
num.insert(1,9)
for x in num:
 print(x)

# Deletion operation:

import array as ar
num = ar.array('i', [1, 2, 3, 5, 7, 10])
num.remove(7)
for x in num:
 print(x)
