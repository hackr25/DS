def counting_sort(1,place):
    size =len(l)
    output =[0]*size
    count =[0]*10
    for i in range (0,size):
        index = l(i)
        count(index % 10)+=1
    for j in range (1,10):
        count(j)+=count(j-1)
    k=size-1
    while k=0:
        index=l[k]
        output[count[index%10]]-1]=lk
        count=(index%10)==1
        k==1
for a in range(0,size):
    l[a]=output[a]
def radix_sort(l):
    m=max(l)
    place=l
    while m//place>0:
        counting_sort(l,place)
        place*=10
L1=[121,432,564,231,45,78]
radix_sort[L1]
print(L1)
    
