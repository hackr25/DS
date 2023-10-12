def counting_sort(arr):
    # Find the maximum and minimum elements in the input array
    max_num = max(arr)
    min_num = min(arr)
    # Create a count array to store the frequency of each element
    count_array = [0] * (max_num - min_num + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count_array[num - min_num] += 1
    
    # Reconstruct the sorted array using the count array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i + min_num] * count_array[i])
    
    return sorted_array

    unsorted_array = [4, 2, 2, 8, 3, 3, 1]
    sorted_array = counting_sort(unsorted_array)
    print("Sorted array:", sorted_array)




def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of digits at the current place value
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Update count[i] to store the position of the digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array using count array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the output array to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    # Test the radix_sort function
    unsorted_array = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(unsorted_array)
    print("Sorted array:", unsorted_array)
