'''
Merge two sorted arrays in o(n) time
'''

arr1= [1, 3, 4, 5] 
arr2 = [2, 4, 6, 8] 
arr3 = [None]* (len(arr1)+len(arr2))
i = 0
j = 0
k = 0

while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        arr3[k] = arr1[i]
        i+=1
        k+=1
    else:
        arr3[k] = arr2[j]
        j+=1
        k+=1
while i<len(arr1):
    arr3[k] = arr1[i]
    i+=1
    k+=1
while j<len(arr2):
    arr3[k] = arr2[j]
    j+=1
    k+=1
print(arr3)

    
