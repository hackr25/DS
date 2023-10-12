#Q.1) Write a python program for implementing Linear search in python.

pos=-1
def search(list,n):
    i=0
    while i<len(list):
         if list[i]==n:
             globals()['pos']=i
             return True
         i=i+1
    return False
list=[5,8,6,4,9,2]
n=9
if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")



def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Element found, return its index
    return -1  

    my_list = [4, 2, 7, 1, 9, 5]
    target_element = 7
    result = linear_search(my_list, target_element)
    
    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found in the list.")

