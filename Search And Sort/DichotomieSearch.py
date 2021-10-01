def dicho(L,x) :
    start, end = 0, len(L)-1
    while start <= end :
        middle=(start+end)//2
        if x == L[middle] : return middle
        elif x < L[middle] : end = middle-1
        else : start = middle+1
    return -1 # case x not in L

print(dicho([1,2,3,4,5,6,7,8,9,10,11,22,55,87,96,145,874],11))