def counting_sort(list1):
    size = len(list1)
    output = [0] * size
    count = [0] * 10  

    for i in range(size):
        count[list1[i]] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    a = size - 1
    while a >= 0:
        output[count[list1[a]] - 1] = list1[a]
        count[list1[a]] -= 1
        a -= 1

    for k in range(size):
        list1[k] = output[k]

data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)

print("Sorted array:")
print(data)
               
                  
