def merge_sort(A,startIndex,endIndex):
    if startIndex < endIndex:
        q = (startIndex+endIndex)//2
        merge_sort(A,startIndex,q)
        merge_sort(A,q+1,endIndex)
        merge(A,startIndex,q,endIndex)


def merge(A,startIndex,q,endIndex):
    print startIndex,q, endIndex
    len_array1 = q-startIndex+1
    len_array2 = endIndex-q
    L, R = [], []
    L.extend(range(0,len_array1+1))
    R.extend(range(len_array2+1))
    for i in range(0,len_array1-1):
        L[i] = A[startIndex+i-1]
    for j in range(0,len_array2-1):
        R[j] = A[q+j]
    #print "R: " +str(R)
    L[-1] = 100000000000
    R[-1] = 100000000000
    i = 0
    j = 0
    print A
    for k in range(startIndex,endIndex):
        if L[i]<=R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1


array = [2,5,1,3,7,4,6,9,8]
merge_sort(array,0,len(array)-1)
print array
