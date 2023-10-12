#Q.2) Write a python program for implementing Binary Search  in python.

pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[5,6,8,3,9,1,12]
n=29
if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")



def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the target element is present at the middle
        if arr[mid] == target:
            return mid
        
        # If the target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore right half
        else:
            right = mid - 1
    
    return -1  

    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_element = 7
    result = binary_search(sorted_list, target_element)
    
    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found in the list.")
